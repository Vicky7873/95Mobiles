from sklearn.metrics import r2_score
import pandas as pd
import dagshub
import mlflow
import joblib
import pickle
import json
from src.bike.entity import BikeModelEvalConfig


class BikeModelEval:
    def __init__(self,config:BikeModelEvalConfig):
        self.config = config

    def model_eval(self):
        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        X_test = pd.read_csv(self.config.X_test)
        # X_test = X_test.drop("Unnamed: 0",axis=1)
        y_test = pd.read_csv(self.config.y_test)
        model = joblib.load(self.config.tunned_model)
        X_train = pd.read_csv(self.config.X_train)
        # X_train = X_train.drop("Unnamed: 0",axis=1)
        y_train = pd.read_csv(self.config.y_train)

        mlflow.set_registry_uri(uri=self.config.mlflow_uri)
        mlflow.set_experiment("Bike model evalution")

        with mlflow.start_run():
            self.y_pred_train = model.predict(X_train)
            self.y_pred = model.predict(X_test)

            self.y_train_acc = r2_score(y_train,self.y_pred_train)
            self.y_test_acc = r2_score(y_test,self.y_pred)
            print("test acc: ",r2_score(y_test,self.y_pred))
            print("train acc: ",r2_score(y_train,self.y_pred_train))
            mlflow.log_metric("testing_Acc", self.y_test_acc)
            mlflow.log_metric("training_Acc", self.y_train_acc)


    def save_score(self):
        scores = {
            "train acc " : self.y_train_acc,
            "test_acc ": self.y_test_acc
        }
        with open (self.config.score,'w') as file:
            json.dump(scores,file,indent=4)