from sklearn.preprocessing import StandardScaler,LabelEncoder
import pandas as pd
from src.car.entity import CarFeatureEngConfig

class Carfe:
    def __init__(self,config:CarFeatureEngConfig):
        self.config = config
    
    @staticmethod
    def loadDatset(self):
        df = pd.read_csv(self.config.raw_data_path)
        return df
    
    def feature_eng(self):
        df = self.loadDatset(self)
        print(df.shape)
        cat_cols = []
        num_cols = []

        for col in df.columns:
            if df[col].dtype == 'object':
                cat_cols.append(col)

        for col in df.columns:
            if df[col].dtype == 'int64':
                num_cols.append(col)

        num_cols.remove('selling_price')

        stc = StandardScaler()
        le = LabelEncoder()
        for cols in df[cat_cols]:
            df[cols] = le.fit_transform(df[[cols]])
         
        for cols in df[num_cols]:
            df[cols] = stc.fit_transform(df[[cols]])

        print(df.head(2))

        df.to_csv(self.config.clean_data)