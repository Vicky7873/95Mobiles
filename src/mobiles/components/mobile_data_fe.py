from sklearn.preprocessing import LabelEncoder,StandardScaler
import pandas as pd
from src.mobiles.entity import Mobile_fe_Config

class fe:
    def __init__(self,config: Mobile_fe_Config) :
        self.config = config

    def load_data(self):
        self.df = pd.read_csv(self.config.mobile_cleaned_data)
        return self.df
    
    def transform_data(self):
        le = LabelEncoder()
        stc = StandardScaler()
        df = self.df
        cat_cols = []
        num_cols = []
        for col in df.columns:
            if df[col].dtype == 'object':
                cat_cols.append(col)
            else:
                num_cols.append(col)

        print(cat_cols)
        print(num_cols)

        num_cols.remove('price')

        for col in df[cat_cols]:
            df[col] = le.fit_transform(df[[col]])
        df[num_cols] = stc.fit_transform(df[num_cols])

        df.drop('Unnamed: 0',axis=1,inplace=True)
        df.to_csv(self.config.final_data,index=False)
        print(df.head(2))