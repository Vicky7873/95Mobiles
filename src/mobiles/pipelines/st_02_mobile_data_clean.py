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


STAGE_NAME = "Mobile Data Cleaning"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = MobileDataCleaning_Pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e