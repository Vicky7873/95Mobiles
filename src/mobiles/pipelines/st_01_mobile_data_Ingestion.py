from src.mobiles.config.configuration import ConfigurationManger
from src.mobiles.components.mb_di import MobileDataIngestion
from log import logger

class MobileDataIngestion_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        mb_config = config.get_mobile_data_ingestion()
        mb_di = MobileDataIngestion(config=mb_config)
        mb_di.download_data()