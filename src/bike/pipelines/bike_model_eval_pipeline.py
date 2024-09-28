from src.bike.config.configuration import ConfigurationManger
from src.bike.components.bike_model_eval import BikeModelEval
from log import logger

class BikeEvalPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        eval_config = config.get_model_eval()
        bike_model_config =BikeModelEval(config=eval_config)
        bike_model_config.model_eval()
        bike_model_config.save_score()