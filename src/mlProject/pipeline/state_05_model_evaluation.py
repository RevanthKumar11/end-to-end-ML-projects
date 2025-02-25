import os
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger


os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/RevanthKumar11/end-to-end-ML-projects.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="RevanthKumar11"
os.environ["MLFLOW_TRACKING_PASSWORD"]="86f77ad3096ceb73793d47a4d6e2fe33f40dbc3c"


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e