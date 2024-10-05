from src.laptop.pipelines.st_01_laptop_data_ingestion import Laptop_DI_pipeline
from log import logger


STAGE_NAME = "Laptop Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Laptop_DI_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e
