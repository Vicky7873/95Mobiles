from src.bike.pipelines.bike_data_ingestion import bike_data_ingestion_pipeline
from src.bike.pipelines.bike_feature_eng import bike_feature_eng_pipeline
from src.bike.pipelines.bike_data_splitpipe import Bike_data_split_pipeline
from src.bike.pipelines.bike_tunning_pipeline import Bike_tunning_pipeline
from src.bike.pipelines.bike_model_eval_pipeline import BikeEvalPipeline
from log import logger

STAGE_NAME = "Bike data ingestion config"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = bike_data_ingestion_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e

STAGE_NAME = "Bike Feature engeenering"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = bike_feature_eng_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e


STAGE_NAME = "Bike Data Split"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Bike_data_split_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e

STAGE_NAME = "Bike Model Tunning"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = Bike_tunning_pipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e



STAGE_NAME = "Bike Model eval"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = BikeEvalPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.Exception(e)
    raise e