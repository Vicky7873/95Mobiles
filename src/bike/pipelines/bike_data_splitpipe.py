from src.bike.config.configuration import ConfigurationManger
from src.bike.components.bike_data_split import SplitData


class Bike_data_split_pipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManger()
        sp_config = config.get_data_split_config()
        split = SplitData(config=sp_config)
        split.split_data()
        split.save_data()
        split.remove_unwanted_cols()