from src.laptop.pipelines.st_01_laptop_data_ingestion import Laptop_DI_pipeline
from src.laptop.pipelines.st_02_laptop_data_fe import Laptop_fe_pipeline
from src.laptop.pipelines.st_03_laptop_data_split import Laptop_datasplitpipeline
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



STAGE_NAME = "Laptop Feature Eng"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Laptop_fe_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e

STAGE_NAME = "Laptop Feature Eng"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Laptop_datasplitpipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e
