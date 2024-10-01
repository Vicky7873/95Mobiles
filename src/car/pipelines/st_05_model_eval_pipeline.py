from src.car.components.car_model_eval import ModelEval
from src.car.config.configuration import ConfigurationManger
from log import logger

class CarModelEvalPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        eval_con = config.get_model_eval()
        model_eval = ModelEval(config=eval_con)
        model_eval.model_eval()