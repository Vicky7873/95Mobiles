from src.bike.entity import DatasplitConfig
from sklearn.model_selection import train_test_split
import pandas as pd

class SplitData:
    def __init__(self,config:DatasplitConfig):
        self.config = config
    
    def split_data(self):
        df = pd.read_csv(self.config.feature_eng_data)
        X = df.drop(columns='price')
        y = df['price']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=self.config.test_size,random_state=self.config.random_state)
        print(f"X_train shape:{X_train.shape}")
        print(f"X_test shape:{X_test.shape}")
        print(f"y_train shape:{y_train.shape}")
        print(f"y_test shape:{y_test.shape}")
        return X_train,X_test,y_train,y_test
    
    def save_data(self):
        X_train,X_test,y_train,y_test = SplitData.split_data(self)
        X_train.to_csv(self.config.X_train,index = False)
        X_test.to_csv(self.config.X_test,index = False)
        y_train.to_csv(self.config.y_train,index = False)
        y_test.to_csv(self.config.y_test,index=False)
        print("data save complete")

    def remove_unwanted_cols(self):
        X_train = pd.read_csv(self.config.X_train)
        X_test = pd.read_csv(self.config.X_test)

        X_train.drop(columns='Unnamed: 0').to_csv(self.config.X_train)
        X_test.drop(columns='Unnamed: 0').to_csv(self.config.X_test)
