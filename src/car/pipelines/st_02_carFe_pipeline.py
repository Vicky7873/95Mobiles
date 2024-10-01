from src.car.components.car_featureEng import Carfe
from src.car.config.configuration import ConfigurationManger


class Car_FE_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        fe_config = config.get_Car_fe()
        car_f = Carfe(config=fe_config)
        car_f.feature_eng()