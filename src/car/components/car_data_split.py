from sklearn.model_selection import train_test_split
from src.car.entity import CarDatSPlitConfig
import pandas as pd

class CarDataSplit:
    def __init__(self,config:CarDatSPlitConfig):
        self.config = config
    @staticmethod
    def split_the_data(self):
        df = pd.read_csv(self.config.clean_data)

        X = df.drop(columns='selling_price',axis=1)
        y = df['selling_price']

        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=self.config.test_size,random_state=self.config.random_state)

        return X_train,X_test,y_train,y_test
    
    def save_the_split(self):
        X_train,X_test,y_train,y_test = self.split_the_data(self)
        X_train.to_csv(self.config.X_train,index = False)
        X_test.to_csv(self.config.X_test,index = False)
        y_train.to_csv(self.config.y_train,index = False)
        y_test.to_csv(self.config.y_test,index = False)

        print(X_train.columns)

    def remove_unwanted_cols(self):
        X_train = pd.read_csv(self.config.X_train)
        X_test = pd.read_csv(self.config.X_test)

        X_train.drop(columns='Unnamed: 0',axis=1,inplace=True)
        X_test.drop(columns='Unnamed: 0',axis=1,inplace=True)
        X_train.to_csv(self.config.X_train,index = False)
        X_test.to_csv(self.config.X_test,index = False)

        print("after clean:\n",X_train.head(1))
        print("after clean:\n",X_test.head(1))
