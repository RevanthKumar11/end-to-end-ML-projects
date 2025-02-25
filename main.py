from mlProject import logger
from mlProject.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeLine
from mlProject.pipeline.state_02_data_validation import DataValidationTrainingPipeLine
from mlProject.pipeline.state_03_data_transformation import DataTransformationTrainingPipeLine


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeLine()
    data_ingestion.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\n X=========X')
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data validation stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_validation = DataValidationTrainingPipeLine()
    data_validation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\n X=========X')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_transformation = DataTransformationTrainingPipeLine()
    data_transformation.main()
    logger.info(f'>>>>> stage {STAGE_NAME} completed <<<<< \n\n X=========X')
except Exception as e:
    logger.exception(e)
    raise e