import requests
from src.bike.entity import Bike_DataIngestionConfig

class Bike_DataIngestion:
    def __init__(self,config:Bike_DataIngestionConfig):
        self.config = config

    def download_data(self):
        response = requests.get(self.config.download_url)
        
        with open(self.config.bike_raw_data,'wb') as file:
            file.write(response.content)
