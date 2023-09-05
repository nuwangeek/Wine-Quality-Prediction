from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject import logger


STAGE_NAME = "Stage 05: Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>Running {STAGE_NAME} Started!<<<<<<<<<<")
        pipeline = ModelEvaluationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>Running {STAGE_NAME} Completed!<<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e