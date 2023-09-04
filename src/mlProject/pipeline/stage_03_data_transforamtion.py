from mlProject.config.configuration import ConfigurationManager 
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Stage 03: Data Transformation"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/STATUS.txt")) as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                raise Exception("Your Data schema is not valid")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME} : {e}")
            raise e


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>Running {STAGE_NAME} Started!<<<<<<<<<<")
        pipeline = DataTransformationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>>>>>Running {STAGE_NAME} Completed!<<<<<<<<<<<")
    except Exception as e:
        logger.error(f"Error in {STAGE_NAME} : {e}")
        raise e
