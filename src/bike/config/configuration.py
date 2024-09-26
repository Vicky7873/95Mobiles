from src.bike.utils.common import create_directory,read_yaml
from src.bike.constants import *
from src.bike.entity import Bike_DataIngestionConfig,Bike_feature_engg

class ConfigurationManger:
    def __init__(self,confi_filepath = CONFIG_FILE_PATH,param_filepath = PARAMS_FILE_PATH):
        self.config = read_yaml(confi_filepath)
        self.params = read_yaml(param_filepath)

        create_directory([self.config.data_root])
    
    def get_bike_data_ingestion_config(self) -> Bike_DataIngestionConfig:
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        bike_data_config = Bike_DataIngestionConfig(
            root_dir=config.root_dir,
            download_url=config.download_url,
            bike_raw_data=config.bike_raw_data
        )

        return bike_data_config


    def get_feature_eng_config(self) -> Bike_feature_engg:
        config = self.config.feature_engeenering

        create_directory([config.root_dir])

        feature_config = Bike_feature_engg(
            root_dir= config.root_dir,
            bike_raw_data=config.bike_raw_data,
            feature_eng_data = config.feature_eng_data
        )

        return feature_config