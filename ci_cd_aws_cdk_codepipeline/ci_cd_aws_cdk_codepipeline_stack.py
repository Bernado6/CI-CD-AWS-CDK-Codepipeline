from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    Stage,
    Environment,
    pipelines,
    aws_codepipeline as codepipeline,
)
from constructs import Construct
from resource_stack.resource_stack import ResourceStack


class DeployStage(Stage):
    def __init__(self, scope: Construct, id: str, env: Environment, **kwargs):
        super().__init__(scope, id, env = env, **kwargs)
        ResourceStack(self, 'ResourceStack', env=env, stack_name='resource-stack-deploy')

class CiCdAwsCdkCodepipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        git_input = pipelines.CodePipelineSource.connection(
            repo_string="Bernado6/CI-CD-AWS-CDK-Codepipeline",
            branch = "main",
            connection_arn="arn:aws:codestar-connections:us-west-2:102513652042:connection/dd9697f3-116f-44b5-aa8b-6c5f691b46cd"
        )

        code_pipeline = codepipeline.Pipeline(
            self,
            "Pipeline",
            pipeline_name="test-pipeline",
            cross_account_keys=False
        )
        
        synth_step = pipelines.ShellStep(
            id="Synth",
            install_commands=[
                "pip install -r requirements.txt"
                ],
            commands= [
                "npx cdk synth"
            ],
            input=git_input
            
        )
        
        pipeline = pipelines.CodePipeline(
            self,
            "CodePipeline",
            self_mutation=True,
            code_pipeline=code_pipeline,
            synth=synth_step
        )
        
        
        deployment_wave = pipeline.add_wave("DeploymentWave")
        
        deployment_wave.add_stage(
            DeployStage(
                self,
                "DeployStage",
                env=(Environment(
                    account="102513652042",
                    region="us-east-1"
                    ))
                )
            )
