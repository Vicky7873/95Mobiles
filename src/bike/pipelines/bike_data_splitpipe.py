from src.bike.config.configuration import ConfigurationManger
from src.bike.components.bike_data_split import SplitData
from log import logger

class Bike_data_split_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        sp_config = config.get_data_split_config()
        split = SplitData(config=sp_config)
        split.split_data()
        split.save_data()
        split.remove_unwanted_cols()

STAGE_NAME = "Bike Data Split"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Bike_data_split_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e