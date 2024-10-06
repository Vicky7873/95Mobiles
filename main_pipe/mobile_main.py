from src.mobiles.pipelines.st_01_mobile_data_Ingestion import MobileDataIngestion_pipeline
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