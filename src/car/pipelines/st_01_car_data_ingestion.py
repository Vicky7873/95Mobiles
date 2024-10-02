from src.car.components.car_data_ingestion import CarData
from src.car.config.configuration import ConfigurationManger
from log import logger


class car_data_ingestion_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        data_config = config.get_data_ingestion()
        car_data = CarData(config=data_config)
        car_data.download_the_data()



STAGE_NAME = "Car data ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = car_data_ingestion_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e