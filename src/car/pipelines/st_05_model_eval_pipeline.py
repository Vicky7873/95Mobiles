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



STAGE_NAME = "Car model eval"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = CarModelEvalPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e