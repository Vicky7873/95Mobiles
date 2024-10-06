import requests
from src.mobiles.entity import MobileDataIngestionConfig


class MobileDataIngestion:
    def __init__(self,config:MobileDataIngestionConfig ) :
        self.config = config
    
    def download_data(self):
        response = requests.get(self.config.download_url)
        with open (self.config.mobile_raw_data,'wb') as file:
            file.write(response.content)