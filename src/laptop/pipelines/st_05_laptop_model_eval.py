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