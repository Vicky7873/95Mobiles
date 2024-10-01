from src.car.components.car_model_training import ModelTrain
from src.car.config.configuration import ConfigurationManger
from log import logger

class CarModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        model_config = config.get_model_trained()
        model_train = ModelTrain(config=model_config)
        model_train.get_model_train()
        model_train.save_model()
