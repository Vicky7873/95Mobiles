from src.bike.components.bike_tunning import BikeTunning
from src.bike.config.configuration import ConfigurationManger
from log import logger

class Bike_tunning_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        bike_config = config.get_model_tunned()
        BikeModel = BikeTunning(config=bike_config)
        BikeModel.tunned_model()
    