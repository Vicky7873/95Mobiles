from src.bike.entity import Bike_feature_engg
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,StandardScaler


class feature_eng:
    cat_cols = []
    num_cols = []
    def __init__(self,config:Bike_feature_engg):
        self.config = config

    def load_data(self):
        self.df = pd.read_csv(self.config.bike_raw_data)
        return self.df
    
    def datatypechange(self):
        self.df['power'] = self.df['power'].astype(int)
        print(self.df['power'].dtypes)
    
    def make_list_as_per_object(self):
        for cols in self.df.columns:
            if self.df[cols].dtypes == 'float64' or self.df[cols].dtypes == 'int64':
                feature_eng.num_cols.append(cols)
            elif self.df[cols].dtypes == 'object':
                feature_eng.cat_cols.append(cols)
        print(feature_eng.cat_cols,feature_eng.num_cols)

    def short_the_city_column(self):
        for city,count in self.df['city'].value_counts().items():
            if count <= 900:
                self.df['city'] = self.df['city'].replace(city,"others")
        print(self.df['city'].nunique())
    
    def encode_cat_cols(self):
        le = LabelEncoder()
        for cols in feature_eng.cat_cols:
            self.df[cols] = le.fit_transform(self.df[cols])
            print(self.df.head(2))
    
    def encode_num_cols(self):
        stc = StandardScaler()
        feature_eng.num_cols.remove('price')
        feature_eng.num_cols.remove('age')
        for cols in feature_eng.num_cols:
            self.df[cols] = stc.fit_transform(self.df[[cols]])
        print(self.df.head(2))

    def save_the_transformed_data(self):
        self.df.to_csv(self.config.feature_eng_data)