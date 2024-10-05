from src.laptop.config.configuration import ConfigurationManger
from src.laptop.components.laptop_datasplit import LaptopDatasplit
from log import logger

class Laptop_datasplitpipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManger()
        split_config = config.get_laptop_data_split()
        ld_split = LaptopDatasplit(config=split_config)
        ld_split.load_data()
        ld_split.Split_the_data()
        ld_split.remove_unwanted_cols_and_save()