from src.car.utils.common import read_yaml,create_directory
from src.car.constants import *
from src.car.entity import CarDataIngestionConfig,CarFeatureEngConfig,CarDatSPlitConfig,CarModelConfig,CarModelevalConfig


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
    

    def get_Car_fe(self)-> CarFeatureEngConfig:
        config = self.config.car_fe
        create_directory([config.root_dir])

        Car_fe = CarFeatureEngConfig(
            root_dir=config.root_dir,
            raw_data_path = config.raw_data_path,
            clean_data = config.clean_data
        )
        return Car_fe
    


    def get_data_split(self)->CarDatSPlitConfig:
        config = self.config.car_data_split
        params = self.params.split

        create_directory([config.root_dir])

        get_ds = CarDatSPlitConfig(
            root_dir=config.root_dir,
            clean_data = config.clean_data,
            X_train = config.X_train,
            X_test = config.X_test,
            y_train = config.y_train,
            y_test = config.y_test,
            test_size = params.test_size,
            random_state = params.random_state
        )

        return get_ds
    


    def get_model_trained(self) -> CarModelConfig:
        config = self.config.Model_Building
        params = self.params.grid

        create_directory([config.root_dir])

        model_train = CarModelConfig(
            root_dir=config.root_dir,
            X_train=config.X_train,
            X_test=config.X_test,
            y_train=config.y_train,
            y_test=config.y_test,
            model_save = config.model_save,
            model_for_train = config.model_for_train,
            fit_intercept = params.fit_intercept,
            n_estimators = params.n_estimators,
            criterion = params.criterion,
            bootstrap = params.bootstrap,
            oob_score = params.oob_score,
            splitter = params.splitter
        )

        return model_train
    


    def get_model_eval(self) -> CarModelevalConfig:
         config = self.config.model_eval
         create_directory([config.root_dir])

         modelevalconfig = CarModelevalConfig(
             root_dir=config.root_dir,
             X_train=config.X_train,
             X_test = config.X_test,
             y_train=config.y_train,
             y_test = config.y_test,
             model_for_train = config.model_for_train,
             save_score = config.save_score
         )

         return modelevalconfig