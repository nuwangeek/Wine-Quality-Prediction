from mlProject.config.configuration import ConfigurationManager 
from mlProject.components.model_trainer import ModelTrainer
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Stage 04: Model Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>Running {STAGE_NAME} Started!<<<<<<<<<<")
        pipeline = ModelTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>Running {STAGE_NAME} Completed!<<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e