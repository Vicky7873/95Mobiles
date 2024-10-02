from src.bike.components.bike_fe import feature_eng
from src.bike.config.configuration import ConfigurationManger
from log import logger


class bike_feature_eng_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        fe_config = config.get_feature_eng_config()
        fe = feature_eng(config=fe_config)
        fe.load_data()
        fe.datatypechange()
        fe.make_list_as_per_object()
        fe.short_the_city_column()
        fe.encode_cat_cols()
        fe.encode_num_cols()
        fe.save_the_transformed_data()

STAGE_NAME = "Bike Feature engeenering"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>>>>>stage {STAGE_NAME} Started<<<<<<<<")
    obj = bike_feature_eng_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
