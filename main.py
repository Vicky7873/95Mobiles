from src.bike.pipelines.bike_data_ingestion import bike_data_ingestion_pipeline
from log import logger

STAGE_NAME = "Bike data ingestion config"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = bike_data_ingestion_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e