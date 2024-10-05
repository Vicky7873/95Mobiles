from src.laptop.components.laptop_dataingestion import Laptop_DataIngestion
from src.laptop.config.configuration import ConfigurationManger
from log import logger

class Laptop_DI_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        laptop_config = config.get_laptop_data_ingestion()
        ld = Laptop_DataIngestion(config=laptop_config)
        ld.download_data()
    