import pandas as pd
from src.mobiles.entity import Mobile_Data_Cleaning_Config

class DataCleaning:
    def __init__(self,config:Mobile_Data_Cleaning_Config):
        self.config = config
    
    def load_data(self):
        self.df = pd.read_csv(self.config.mobile_raw_data)
        return self.df
    
    def columns_cleaning(self):
        df = self.df
        df = df.rename(columns={'Price ($)':'price'})
        df = df.rename(columns={'Screen Size (inches)':'screen_size','Camera (MP)':'camera','Battery Capacity (mAh)':'battery'})
        df.columns=df.columns.str.replace(' ','')
        return df
    
    def clean_data(self):
        df = self.columns_cleaning()
        df['price'] = df['price'].str.replace(r'\D', '', regex=True)
        df['price']=df['price'].astype('float')
        df['price']=df['price'].multiply(84)
        df['camera'] = df['camera'].str.replace('MP','')
        df['RAM'] = df['RAM'].str.replace(r'\D', '', regex=True)
        df['Storage'] = df['Storage'].str.replace(r'\D', '', regex=True)
        df['camera'] = df['camera'].str.replace(' ','')
        print(df.head(10))

        df.to_csv(self.config.mobile_cleaned_data)