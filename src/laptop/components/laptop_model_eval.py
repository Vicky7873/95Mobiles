from sklearn.metrics import r2_score
import pandas as pd
import mlflow
import dagshub
import joblib
import json
from src.laptop.entity import laptop_modelevalconfig



class ModelEval:
    def __init__(self,config:laptop_modelevalconfig):
        self.config = config
    
    def model_evl(self):
        X_train = pd.read_csv(self.config.X_train)
        X_test = pd.read_csv(self.config.X_test)
        y_train = pd.read_csv(self.config.y_train)
        y_test = pd.read_csv(self.config.y_test)
        
        model = joblib.load(self.config.model_for_train)

        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        mlflow.set_registry_uri("https://dagshub.com/Vicky7873/95Mobiles.mlflow")
        mlflow.set_experiment("laptop model eval")

        with mlflow.start_run():
            train_acc = model.score(X_train,y_train)
            print(f"my training acc: {train_acc}")
            y_pred = model.predict(X_test)
            test_acc = r2_score(y_test,y_pred)
            print(f"my testing acc: {test_acc}")

            score = {
                "train score: ": train_acc,
                "test score: ": test_acc
            }

            mlflow.log_metric("training acc ",train_acc)
            mlflow.log_metric("test acc ",test_acc)

            with open(self.config.save_score,'w') as file:
                json.dump(score,file,indent=4)
