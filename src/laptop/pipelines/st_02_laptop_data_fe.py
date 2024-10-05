from src.laptop.components.laptop_fe import laptop_fe
from src.laptop.config.configuration import ConfigurationManger
from log import logger

class Laptop_fe_pipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        fe_config = config.get_Fe_config()
        laptop = laptop_fe(config=fe_config)
        laptop.load_data()
        laptop.drop_and_rename_cols_change_cols_value()
        laptop.transform_data()
        laptop.save_data()


STAGE_NAME = "Laptop Feature Eng"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Laptop_fe_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e