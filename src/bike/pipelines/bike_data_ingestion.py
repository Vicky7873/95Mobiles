from src.bike.config.configuration import ConfigurationManger
from src.bike.components.bike_data_ingestion import Bike_DataIngestion
from log import logger

class bike_data_ingestion_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        bike_di_config = config.get_bike_data_ingestion_config()
        bike_di = Bike_DataIngestion(config=bike_di_config)
        bike_di.download_data()

STAGE_NAME = " Bike Data Ingestion"
if __name__ == "__main__":
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>>>>>stage {STAGE_NAME} Started<<<<<<<<")
        obj = bike_data_ingestion_pipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
    except Exception as e:
        logger.exception(e)
        raise e