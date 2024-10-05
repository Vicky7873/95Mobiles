from sklearn.preprocessing import StandardScaler,LabelEncoder
import pandas as pd
from src.laptop.entity import Laptop_feConfig

class laptop_fe:
    def __init__(self,config:Laptop_feConfig):
        self.config = config

    def load_data(self):
        df = pd.read_csv(self.config.laptop_raw_data,encoding='ISO-8859-1')
        return df
    
    def drop_and_rename_cols_change_cols_value(self):
        df = self.load_data()
        df.drop(columns='laptop_ID',axis=1,inplace=True)
        df = df.rename(columns={"Price_euros":"price"})
        df['price'] = df['price'].multiply(92)
        df['Weight'] = df['Weight'].str.replace("kg",'').astype(float)
        return df
    
    def transform_data(self):
        df = self.drop_and_rename_cols_change_cols_value()
        le = LabelEncoder()
        stc = StandardScaler()
        cat_cols = []
        num_cols = []

        for col in df.columns:
            if df[col].dtype == 'float64':
                num_cols.append(col)
            elif df[col].dtype == 'object':
                cat_cols.append(col)
        
        num_cols.remove('price')

        for col in df[num_cols]:
            df[col] = stc.fit_transform(df[[col]])
        
        for col in df[cat_cols]:
            df[col] = le.fit_transform(df[col])
        
        print(df.head(2))
        return df
    
    def save_data(self):
        df = self.transform_data()
        df.to_csv(self.config.laptop_cleaned_data)
        print("data was saved")