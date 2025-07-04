# infrastructure/monitoring_stack.py
import os

from aws_cdk import Duration, Stack
from aws_cdk import aws_budgets as budgets
from aws_cdk import aws_cloudwatch as cloudwatch
from aws_cdk import aws_cloudwatch_actions as cw_actions
from aws_cdk import aws_sns as sns
from aws_cdk import aws_sns_subscriptions as sns_subscriptions
from constructs import Construct
from dotenv import load_dotenv

load_dotenv()


class MonitoringStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs: object) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # SNS Topic for alerts
        alert_topic = sns.Topic(
            self, "CostAlertTopic",
            display_name="Cost Optimization Alerts"
        )
        
        # Subscribe to the topic using an email address from environment variable 
        # Ensure the EMAIL environment variable is set
        # Needs confirmation via email after deployment
        alert_topic.add_subscription(
            sns_subscriptions.EmailSubscription(os.getenv("EMAIL")) 
        )

        
        # Cost Budget Alert
        budgets.CfnBudget(
            self, "MonthlyBudget",
            budget={
                "budgetName": "Monthly-AWS-Budget",
                "budgetLimit": {
                    "amount": 50,  # $50 monthly limit
                    "unit": "USD"
                },
                "timeUnit": "MONTHLY",
                "budgetType": "COST"
            },
            notifications_with_subscribers=[
                {
                    "notification": {
                        "notificationType": "ACTUAL",
                        "comparisonOperator": "GREATER_THAN",
                        "threshold": 80  # Alert at 80% of budget ($40)
                    },
                    "subscribers": [
                        {
                            "subscriptionType": "EMAIL",
                            "address": os.getenv("EMAIL", "")  # Use environment variable for email
                        }
                    ]
                },
                {
                    "notification": {
                        "notificationType": "FORECASTED",
                        "comparisonOperator": "GREATER_THAN",
                        "threshold": 100  # Alert when forecasted to exceed budget
                    },
                    "subscribers": [
                        {
                            "subscriptionType": "EMAIL",
                            "address": os.getenv("EMAIL", "")  # Use environment variable for email
                        }
                    ]
                }
            ]
        )
        
        # CloudWatch Billing Alarm
        billing_alarm = cloudwatch.Alarm(
            self, "BillingAlarm",
            metric=cloudwatch.Metric(
                namespace="AWS/Billing",
                metric_name="EstimatedCharges",
                dimensions_map={
                    "Currency": "USD"
                },
                statistic="Maximum",
                period=Duration.hours(6)
            ),
            threshold=30,  # $30 threshold
            evaluation_periods=1,
            alarm_description="Alert when estimated charges exceed $30"
        )
        
        billing_alarm.add_alarm_action(
            cw_actions.SnsAction(alert_topic)
        )
        
        # Custom Dashboard
        dashboard = cloudwatch.Dashboard(
            self, "CostDashboard",
            dashboard_name="Cost-Optimization-Dashboard"
        )
        
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Estimated Monthly Charges",
                left=[billing_alarm.metric],
                width=12,
                height=6,
                left_y_axis=cloudwatch.YAxisProps(
                    label="USD",
                    min=0,
                    show_units=True
            )
        )
        )