from src.mobiles.components.mobile_datasplit import mobile_datasplit
from src.mobiles.config.configuration import ConfigurationManger
from log import logger


class Mobile_datasplit_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        split = config.get_data_split()
        ds = mobile_datasplit(config=split)
        ds.load_data()
        ds.split_data()
        ds.save_data()



STAGE_NAME = "Mobile data split"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Mobile_datasplit_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e