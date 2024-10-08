from src.mobiles.components.mobile_model_eval import MobilemodelEval
from src.mobiles.config.configuration import ConfigurationManger
from log import logger

class MobileModelEvalPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        eval_con = config.get_model_eval()
        model_eval = MobilemodelEval(eval_con)
        model_eval.model_eval()
    


STAGE_NAME = "Mobile model eval"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = MobileModelEvalPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e