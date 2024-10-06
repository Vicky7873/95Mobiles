from src.mobiles.utils.common import read_yaml,create_directory
from src.mobiles.constants import *
from src.mobiles.entity import MobileDataIngestionConfig,Mobile_Data_Cleaning_Config,Mobile_fe_Config,mobile_datasplitconfig,mobile_Modeltrainconfig,mobile_model_eval_config

class ConfigurationManger:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH) :
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
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
    

    def get_mobile_fe(self)->Mobile_fe_Config:
        config = self.config.feature_eng
        create_directory([config.root_dir])

        model_fe = Mobile_fe_Config(
            root_dir=config.root_dir,
            mobile_cleaned_data=config.mobile_cleaned_data,
            final_data = config.final_data
        )

        return model_fe
    



    def get_data_split(self) -> mobile_datasplitconfig:
        config = self.config.data_split
        params = self.params.split

        create_directory([config.root_dir])

        model_datasplit = mobile_datasplitconfig(
            root_dir=config.root_dir,
            X_train=config.X_train,
            X_test=config.X_test,
            y_train=config.y_train,
            y_test=config.y_test,
            test_size=params.test_size,
            random_state=params.random_state,
            final_data=config.final_data
        )
        return model_datasplit
    

    def get_model_train(self)->mobile_Modeltrainconfig:
        config = self.config.model_train
        create_directory([config.root_dir])
        model_train = mobile_Modeltrainconfig(
            root_dir=config.root_dir,
            X_train=config.X_train,
            X_test=config.X_test,
            y_train=config.y_train,
            y_test=config.y_test,
            save_model=config.save_model,
            model_for_train=config.model_for_train
        )
        return model_train
    


    def get_model_eval(self) -> mobile_model_eval_config:
        config = self.config.model_eval
        create_directory([config.root_dir])

        model_eval = mobile_model_eval_config(
            root_dir=config.root_dir,
            X_train = config.X_train,
            X_test = config.X_test,
            y_train=config.y_train,
            y_test=config.y_test,
            save_score=config.save_score,
            model_for_train=config.model_for_train
        )

        return model_eval