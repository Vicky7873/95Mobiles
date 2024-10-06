from src.mobiles.pipelines.st_01_mobile_data_Ingestion import MobileDataIngestion_pipeline
from src.mobiles.pipelines.st_02_mobile_data_clean import MobileDataCleaning_Pipeline
from src.mobiles.pipelines.st_03_mobile_fe import mobile_fe_pipeline
from src.mobiles.pipelines.st_04_mobile_data_split import Mobile_datasplit_pipeline
from log import logger

STAGE_NAME = "Mobile Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = MobileDataIngestion_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Mobile Data Cleaning"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = MobileDataCleaning_Pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Mobile fe"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = mobile_fe_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Mobile data split"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Mobile_datasplit_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e