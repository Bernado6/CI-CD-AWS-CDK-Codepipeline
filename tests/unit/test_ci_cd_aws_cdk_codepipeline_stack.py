import aws_cdk as core
import aws_cdk.assertions as assertions

from ci_cd_aws_cdk_codepipeline.ci_cd_aws_cdk_codepipeline_stack import CiCdAwsCdkCodepipelineStack

# example tests. To run these tests, uncomment this file along with the example
# resource in ci_cd_aws_cdk_codepipeline/ci_cd_aws_cdk_codepipeline_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CiCdAwsCdkCodepipelineStack(app, "ci-cd-aws-cdk-codepipeline")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
