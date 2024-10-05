from sklearn.model_selection import train_test_split
import pandas as pd
from src.laptop.entity import Laptop_datasplit

class LaptopDatasplit:
    def __init__(self,config:Laptop_datasplit):
        self.config = config
    
    def load_data(self):
        self.df = pd.read_csv(self.config.laptop_cleaned_data)
        return self.df
    
    def Split_the_data(self):
        df = self.df
        X=df.drop('price',axis=1)
        y=df['price']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=self.config.random_state,random_state=self.config.random_state)
        return X_train,X_test,y_train,y_test
    
    def remove_unwanted_cols_and_save(self):
        X_train,X_test,y_train,y_test = self.Split_the_data()
        X_train.drop('Unnamed: 0',inplace=True,axis=1)
        X_test.drop('Unnamed: 0',axis=1,inplace=True)
        X_train.to_csv(self.config.X_train,index=False)
        X_test.to_csv(self.config.X_test,index=False)
        y_train.to_csv(self.config.y_train,index=False)
        y_test.to_csv(self.config.y_test,index=False)
        print(X_train.head(2))
    