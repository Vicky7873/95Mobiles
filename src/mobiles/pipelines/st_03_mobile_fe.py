from src.mobiles.components.mobile_data_fe import fe
from src.mobiles.config.configuration import ConfigurationManger
from log import logger

class mobile_fe_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        fe_config = config.get_mobile_fe()
        fe_do = fe(config=fe_config)
        fe_do.load_data()
        fe_do.transform_data()

    
STAGE_NAME = "Mobile fe"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = mobile_fe_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e