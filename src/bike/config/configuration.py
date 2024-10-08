from src.bike.utils.common import create_directory,read_yaml
from src.bike.constants import *
from src.bike.entity import Bike_DataIngestionConfig,Bike_feature_engg,DatasplitConfig,BikeModelTuningConfig,BikeModelEvalConfig

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
    


    def get_data_split_config(self) -> DatasplitConfig:
        config = self.config.splliting_data
        params = self.params.split
        create_directory([config.root_dir])

        split_config = DatasplitConfig(
            root_dir = config.root_dir,
            feature_eng_data = config.feature_eng_data,
            X_train = config.X_train,
            X_test = config.X_test,
            y_train = config.y_train,
            y_test = config.y_test,
            test_size = params.test_size,
            random_state = params.random_state
        )

        return split_config
    


    def get_model_tunned(self) -> BikeModelTuningConfig:
        config = self.config.hyper_tune
        params = self.params.model

        create_directory([config.root_dir])

        tunning_config = BikeModelTuningConfig(
            root_dir=config.root_dir,
            X_train = config.X_train,
            X_test=config.X_test,
            y_train=config.y_train,
            y_test=config.y_test,
            tunned_model = config.tunned_model,
            n_estimators = params.n_estimators,
            bootstrap = params.bootstrap,
            criterion=params.criterion,
            oob_score=params.oob_score,
            mlflow_uri="https://dagshub.com/Vicky7873/95Mobiles.mlflow"

        )

        return tunning_config
    


    def get_model_eval(self)-> BikeModelEvalConfig:
        config = self.config.model_eval

        create_directory([config.root_dir])

        model_eval = BikeModelEvalConfig(
            root_dir=config.root_dir,
            X_test=config.X_test,
            y_test=config.y_test,
            tunned_model=config.tunned_model,
            mlflow_uri="https://dagshub.com/Vicky7873/95Mobiles.mlflow",
            X_train=config.X_train,
            y_train=config.y_train,
            score= config.score
        )

        return model_eval