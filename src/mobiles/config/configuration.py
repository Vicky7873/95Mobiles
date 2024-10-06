from src.mobiles.utils.common import read_yaml,create_directory
from src.mobiles.constants import *
from src.mobiles.entity import MobileDataIngestionConfig,Mobile_Data_Cleaning_Config

class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH) :
        self.config = read_yaml(config_filepath)
        create_directory([self.config.data_root])

    def get_mobile_data_ingestion(self)->MobileDataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        model_dataingestion = MobileDataIngestionConfig(
            root_dir=config.root_dir,
            download_url=config.download_url,
            mobile_raw_data=config.mobile_raw_data
        )

        return model_dataingestion


    def get_mobile_data_cleaning(self)->Mobile_Data_Cleaning_Config:
        config = self.config.data_cleaning
        create_directory([config.root_dir])

        model_datacleaning = Mobile_Data_Cleaning_Config(
            root_dir=config.root_dir,
            mobile_raw_data=config.mobile_raw_data,
            mobile_cleaned_data=config.mobile_cleaned_data
        )

        return model_datacleaning