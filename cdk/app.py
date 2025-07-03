#!/usr/bin/env python3
import aws_cdk as cdk
from infrastructure.compute_stack import ComputeStack
from infrastructure.monitoring_stack import MonitoringStack
from infrastructure.vpc_stack import VpcStack

app = cdk.App()

# Deploy infrastructure stacks
vpc_stack = VpcStack(app, "VpcStack")
compute_stack = ComputeStack(app, "ComputeStack", vpc=vpc_stack.vpc)
monitoring_stack = MonitoringStack(app, "MonitoringStack")

app.synth()