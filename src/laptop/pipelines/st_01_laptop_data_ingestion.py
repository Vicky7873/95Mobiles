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



STAGE_NAME = "Laptop Data Ingestion"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Laptop_DI_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e
    