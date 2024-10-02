from src.car.components.car_data_split import CarDataSplit
from src.car.config.configuration import ConfigurationManger
from log import logger

class CarDatSplit_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        split_config = config.get_data_split()
        car_split = CarDataSplit(config=split_config)
        car_split.save_the_split()
        car_split.remove_unwanted_cols()


STAGE_NAME = "Car data split"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = CarDatSplit_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e