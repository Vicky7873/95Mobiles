from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd
import joblib
import mlflow
import dagshub
from src.car.entity import CarModelConfig


class ModelTrain:
    def __init__(self,config:CarModelConfig):
        self.config = config

    def get_model_train(self):
        models = {
            "lr":LinearRegression(),
            "rfr":RandomForestRegressor(),
            "dtr":DecisionTreeRegressor()
        }

        grid_params = {
            "lr":{
                "fit_intercept":self.config.fit_intercept
            },
            "rfr":{
                "n_estimators":self.config.n_estimators,
                "criterion": self.config.criterion,
                "bootstrap" : self.config.bootstrap,
                "oob_score" : self.config.oob_score

            },
            "dtr":{
                "criterion": self.config.criterion,
                "splitter":self.config.splitter
            }
        }

        X_train = pd.read_csv(self.config.X_train)
        y_train = pd.read_csv(self.config.y_train)

        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        mlflow.set_registry_uri("https://dagshub.com/Vicky7873/95Mobiles.mlflow")
        mlflow.set_experiment("Car Model Training")

        compare_score = -float("inf")
        with mlflow.start_run():
            for model_name,model in models.items():
                gdr_train = GridSearchCV(model,param_grid=grid_params[model_name],cv=5)
                gdr_train.fit(X_train,y_train)

                print("Best parameters: ", gdr_train.best_params_)
                print("best score: ", gdr_train.best_score_)
                print("best estimator: ", gdr_train.best_estimator_)

                mlflow.log_metric(f"{model_name}_best_score", gdr_train.best_score_)
                mlflow.log_params({f"{model_name}_best_params": gdr_train.best_params_})

                if gdr_train.best_score_ > compare_score:
                    compare_score = gdr_train.best_score_
                    self.best_model = gdr_train.best_estimator_
                    print("Best Model Type:", self.best_model)
    
    def save_model(self):
        model = self.best_model
        print(type(model).__name__)
        joblib.dump(model,self.config.model_save)
        joblib.dump(model,self.config.model_for_train)
        print(f"Model: {model} was saved to its path")