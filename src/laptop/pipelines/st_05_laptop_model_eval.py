from src.laptop.config.configuration import ConfigurationManger
from src.laptop.components.laptop_model_eval import ModelEval
from log import logger

class Model_evalPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        eval_config = config.get_model_eval()
        me = ModelEval(config=eval_config)
        me.model_evl()



STAGE_NAME = "Laptop model Eval"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Model_evalPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e