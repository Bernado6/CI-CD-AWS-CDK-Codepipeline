#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ci_cd_aws_cdk_codepipeline.ci_cd_aws_cdk_codepipeline_stack import CiCdAwsCdkCodepipelineStack


app = cdk.App()
CiCdAwsCdkCodepipelineStack(app, "CiCdAwsCdkCodepipelineStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account='102513652042', region='us-east-1'),
    stack_name = 'github-codepipeline-stack'

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

cdk.Tags.of(app).add(key="feature", value="resource_stack")
cdk.Tags.of(app).add(key="Contact", value="mlengineer@gmail.com")
cdk.Tags.of(app).add(key="Team", value="ML_Team")

app.synth()
