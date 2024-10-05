from src.laptop.constants import *
from src.laptop.utils.common import read_yaml,create_directory
from src.laptop.entity import LaptopDataIngestionConfig


class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH) :
        self.config = read_yaml(config_filepath)
        create_directory([self.config.data_root])
        
    def get_laptop_data_ingestion(self):
        config = self.config.data_ingestion
        create_directory([config.root_dir])

        laptopdata = LaptopDataIngestionConfig(
            root_dir=config.root_dir,
            download_url = config.download_url,
            laptop_raw_data = config.laptop_raw_data
        )

        return laptopdata

