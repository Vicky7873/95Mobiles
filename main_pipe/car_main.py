from src.car.pipelines.st_01_car_data_ingestion import car_data_ingestion_pipeline
from src.car.pipelines.st_02_carFe_pipeline import Car_FE_pipeline
from src.car.pipelines.st_03_car_data_splitpipeline import CarDatSplit_pipeline
from log import logger


STAGE_NAME = "Car data ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = car_data_ingestion_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e


STAGE_NAME = "Car Feature Eng"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Car_FE_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e


STAGE_NAME = "Car data split"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = CarDatSplit_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e