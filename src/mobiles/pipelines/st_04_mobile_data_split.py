from src.mobiles.components.mobile_datasplit import mobile_datasplit
from src.mobiles.config.configuration import ConfigurationManger


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