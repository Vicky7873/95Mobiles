from src.bike.config.configuration import ConfigurationManger
from src.bike.components.bike_data_ingestion import Bike_DataIngestion

class bike_data_ingestion_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        bike_di_config = config.get_bike_data_ingestion_config()
        bike_di = Bike_DataIngestion(config=bike_di_config)
        bike_di.download_data()
        