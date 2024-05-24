from aws_cdk import (
    Stack,
    aws_sqs as sqs,
    Duration,
    aws_lambda as function_lambda,
    aws_iam as iam,
    aws_s3 as s3
)

from  constructs import Construct

class ResourceStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        queue = sqs.Queue(
            self, 
            "AWSCodePipelineAppDemoQueue",
            visibility_timeout=Duration.seconds(300),
            queue_name="demo_queue"
        )
        
        function = function_lambda.Function(
            self,
            "DemoCDKGitHubLambda",
            function_name="codepipeline_lambda",
            runtime=function_lambda.Runtime.PYTHON_3_9,
            code=function_lambda.Code.from_asset('./lambda_code_demo'),
            handler="demo_lambda.lambda_handler"
        )
        
        bucket = s3.Bucket(
            self,
            "myfirstbucket",
            versioned=True,
            bucket_name="demo-bucket-beyond-the-cloud-1286381",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL)
    