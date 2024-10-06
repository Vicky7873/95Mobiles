from src.mobiles.components.mobile_modeltrain import Model_train
from src.mobiles.config.configuration import ConfigurationManger
from log import logger

class MobileModeltrain:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        model_con = config.get_model_train()
        model = Model_train(config=model_con)
        model.train_model()
        model.save_model()


STAGE_NAME = "Mobile model train"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = MobileModeltrain()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e