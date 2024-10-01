import requests
from src.car.entity import CarDataIngestionConfig


class CarData:
    def __init__(self,config:CarDataIngestionConfig ) -> None:
        self.config = config

    def download_the_data(self):
        response = requests.get(self.config.download_uri)

        with open (self.config.raw_data_path, 'wb') as file:
            file.write(response.content)