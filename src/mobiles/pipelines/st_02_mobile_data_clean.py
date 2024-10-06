from src.mobiles.components.mobile_data_clean import DataCleaning
from src.mobiles.config.configuration import ConfigurationManger
from log import logger

class MobileDataCleaning_Pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        
        data_cleaning = DataCleaning(config.get_mobile_data_cleaning())
        data_cleaning.load_data()
        data_cleaning.columns_cleaning()
        data_cleaning.clean_data()
        logger.info("Mobile data cleaned successfully")