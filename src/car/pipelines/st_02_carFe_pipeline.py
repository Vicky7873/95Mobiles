from src.car.components.car_featureEng import Carfe
from src.car.config.configuration import ConfigurationManger
from log import logger


class Car_FE_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        fe_config = config.get_Car_fe()
        car_f = Carfe(config=fe_config)
        car_f.feature_eng()



STAGE_NAME = "Car Feature Eng"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Car_FE_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e