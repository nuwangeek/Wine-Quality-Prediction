from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = "Stage 01: Data Ingestion"
try:
    logger.info(f">>>>>>>>>Running {STAGE_NAME} Started!<<<<<<<<<<")
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
    logger.info(f">>>>>>>>>Running {STAGE_NAME} Completed!<<<<<<<<<<<")
except Exception as e:
    logger.error(f"Error in {STAGE_NAME} : {e}")
    raise e