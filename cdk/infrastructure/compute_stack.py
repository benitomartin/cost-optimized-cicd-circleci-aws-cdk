# infrastructure/compute_stack.py
from typing import Any

from aws_cdk import Duration, Stack, Tags
from aws_cdk import aws_autoscaling as autoscaling
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from constructs import Construct


class ComputeStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Security Group
        security_group = ec2.SecurityGroup(
            self, "WebServerSG",
            vpc=vpc,
            description="Security group for web servers",
            allow_all_outbound=True
        )
        
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            "Allow HTTP traffic"
        )
        
        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22),
            "Allow SSH access"
        )
                
        # IAM Role for EC2 instances
        role = iam.Role(
            self, "EC2Role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchAgentServerPolicy")
            ]
        )
        
        # Launch Template
        launch_template = ec2.LaunchTemplate(
            self, "LaunchTemplate",
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.T3,
                ec2.InstanceSize.MICRO
            ),
            machine_image=ec2.AmazonLinuxImage(
                generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2
            ),
            security_group=security_group,
            role=role,
            user_data=ec2.UserData.for_linux()
        )
        
        # Add simple web server setup
        launch_template.user_data.add_commands(
            "yum update -y",
            "yum install -y httpd",
            "systemctl start httpd",
            "systemctl enable httpd",
            "echo '<h1>Cost-Optimized CI/CD Demo</h1>' > /var/www/html/index.html"
            # Add stress-ng installation
            "amazon-linux-extras install epel -y",
            "yum install -y stress-ng",
            # # Generate CPU load (will trigger scaling)
            # Run stress-ng for 5 minutes on 4 CPU cores in background
            # "stress --cpu 4 --timeout 300s"
        )

        
        # Auto Scaling Group
        self.asg = autoscaling.AutoScalingGroup(
            self, "WebServerASG",
            vpc=vpc,
            launch_template=launch_template,
            min_capacity=1,
            max_capacity=3,
            desired_capacity=1,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PUBLIC
            )
        )
        
        Tags.of(self.asg).add("Name", "CostOptimizedWebServer")
        
        # Target Tracking Scaling Policy
        self.asg.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=70,
            cooldown=Duration.minutes(5)
        )

