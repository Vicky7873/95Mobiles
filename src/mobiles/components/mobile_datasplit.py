from sklearn.model_selection import train_test_split
import pandas as pd
from src.mobiles.entity import mobile_datasplitconfig

class mobile_datasplit:
    def __init__(self,config:mobile_datasplitconfig):
        self.config = config
    
    def load_data(self):
        self.df = pd.read_csv(self.config.final_data)
        return self.df
    
    def split_data(self):
        df = self.df
        X =df.drop('price',axis=1)
        y=df['price']
        self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(X,y,test_size=self.config.test_size,random_state=self.config.random_state)
        return self.X_train,self.X_test,self.y_train,self.y_test
    
    def save_data(self):
        X_train = self.X_train
        X_test = self.X_test
        y_train = self.y_train
        y_test = self.y_test

        X_train.to_csv(self.config.X_train,index=False)
        X_test.to_csv(self.config.X_test,index = False)
        y_train.to_csv(self.config.y_train,index=False)
        y_test.to_csv(self.config.y_test,index=False)
        print(X_train.head(2))
        print(X_test.head(2))
