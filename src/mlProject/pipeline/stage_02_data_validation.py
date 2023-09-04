from mlProject.config.configuration import ConfigurationManager 
from mlProject.components.data_validation import DataValidation
from mlProject import logger


sTAGE_NAME = "Stage 02: Data Validation"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>Running {sTAGE_NAME} Started!<<<<<<<<<<")
        pipeline = DataValidationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>Running {sTAGE_NAME} Completed!<<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Error in {sTAGE_NAME} : {e}")
        raise e