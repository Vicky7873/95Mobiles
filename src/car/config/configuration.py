from src.car.utils.common import read_yaml,create_directory
from src.car.constants import *
from src.car.entity import CarDataIngestionConfig


class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAM_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directory([self.config.data_root])

    def get_data_ingestion(self)-> CarDataIngestionConfig :
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        data_ingestion = CarDataIngestionConfig(
            root_dir=config.root_dir,
            download_uri=config.download_uri,
            raw_data_path=config.raw_data_path
        )

        return data_ingestion