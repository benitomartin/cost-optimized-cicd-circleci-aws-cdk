# infrastructure/vpc_stack.py
from typing import Any

from aws_cdk import (
    Stack,
)
from aws_cdk import (
    aws_ec2 as ec2,
)
from constructs import Construct


class VpcStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Create VPC with public and private subnets
        self.vpc = ec2.Vpc(
            self, "CostOptimizedVPC",
            max_azs=2,
            cidr="10.0.0.0/16",
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="PublicSubnet",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="PrivateSubnet",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24
                )
            ]
        )