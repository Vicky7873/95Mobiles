from src.laptop.constants import *
from src.laptop.utils.common import read_yaml,create_directory
from src.laptop.entity import LaptopDataIngestionConfig,Laptop_feConfig,Laptop_datasplit


class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH) :
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
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
    


    def get_Fe_config(self)->Laptop_feConfig:
        config = self.config.feature_eng
        create_directory([config.root_dir])

        model_feconfig = Laptop_feConfig(
            root_dir=config.root_dir,
            laptop_raw_data = config.laptop_raw_data,
            laptop_cleaned_data = config.laptop_cleaned_data
        )

        return model_feconfig
    


    def get_laptop_data_split(self) -> Laptop_datasplit:
        config = self.config.data_split
        param = self.params.split
        create_directory([config.root_dir])

        model_datasplitConfig = Laptop_datasplit(
            root_dir = config.root_dir,
            laptop_cleaned_data = config.laptop_cleaned_data,
            X_train = config.X_train,
            X_test = config.X_test,
            y_train = config.y_train,
            y_test = config.y_test,
            test_size = param.test_size,
            random_state = param.random_state
        )

        return model_datasplitConfig

