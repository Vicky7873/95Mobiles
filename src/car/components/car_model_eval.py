from sklearn.metrics import r2_score
import pandas as pd
import joblib
import json
import dagshub
import mlflow
from src.car.entity import CarModelevalConfig


class ModelEval:
    def __init__(self,config:CarModelevalConfig):
        self.config = config

    def model_eval(self):
        X_train = pd.read_csv(self.config.X_train)
        X_test = pd.read_csv(self.config.X_test)
        y_train = pd.read_csv(self.config.y_train)
        y_test = pd.read_csv(self.config.y_test)


        model = joblib.load(self.config.model_for_train)

        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        mlflow.set_registry_uri("https://dagshub.com/Vicky7873/95Mobiles.mlflow")
        mlflow.set_experiment("Car Model Eval")

        with mlflow.start_run():
            print("train acc: ",model.score(X_train,y_train))
            train_score = model.score(X_train,y_train)
            y_pred = model.predict(X_test)
            test_acc = r2_score(y_test,y_pred)
            print("test acc: ", test_acc )

            score = {
                "train score: ": train_score,
                "test score: ": test_acc
            }
            mlflow.log_metric("Training_acc",train_score)
            mlflow.log_metric("Testing_acc",test_acc)

        with open (self.config.save_score,"w") as file:
            json.dump(score,file,indent=4)