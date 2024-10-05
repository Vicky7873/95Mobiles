import pandas as pd
import numpy as np
import requests
from src.laptop.entity import LaptopDataIngestionConfig

class Laptop_DataIngestion:
    def __init__(self,config: LaptopDataIngestionConfig):
        self.config = config
    
    def download_data(self):
        response = requests.get(self.config.download_url)

        with open (self.config.laptop_raw_data,"wb") as file:
            file.write(response.content)


