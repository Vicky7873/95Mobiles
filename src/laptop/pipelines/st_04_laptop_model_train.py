from src.laptop.config.configuration import ConfigurationManger
from src.laptop.components.laptop_model_train import Laptop_modeltrain
from log import logger

class Laptop_ModelTrainPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config=ConfigurationManger()
        model_config = config.get_moel_train()
        lp_model = Laptop_modeltrain(config=model_config)
        lp_model.model_train()
        lp_model.model_save()


STAGE_NAME = "Laptop Feature Eng"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Laptop_ModelTrainPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e