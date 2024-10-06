from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import GridSearchCV
import pandas as pd
import joblib
import dagshub
import mlflow
from src.mobiles.entity import mobile_Modeltrainconfig

models = {
    "lr":LinearRegression(),
    "rfr":RandomForestRegressor(),
    "dtr":DecisionTreeRegressor()
}

grid_param = {
    "lr":{
        "fit_intercept":[False,True]
    },
    "rfr":{
        "n_estimators":[15,17,19],
        "criterion": ["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "bootstrap" : [True,False],
        "oob_score" : [True,False]

    },
    "dtr":{
        "criterion": ["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "splitter":["best","random"]
    }
}


class Model_train:
    def __init__(self,config:mobile_Modeltrainconfig ):
        self.config = config
    
    def train_model(self):
        X_train = pd.read_csv(self.config.X_train)
        y_train = pd.read_csv(self.config.y_train)

        best_score = -float("inf")
        self.best_model = None
        best_model_name = None

        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        mlflow.set_registry_uri("https://dagshub.com/Vicky7873/95Mobiles.mlflow")
        mlflow.set_experiment("Mobile model training")
        for model_name,model in models.items():
            models_gdr = GridSearchCV(model,param_grid=grid_param[model_name],cv=5)
            models_gdr.fit(X_train,y_train)
            print("Best parameters: ", models_gdr.best_params_)
            print("best score: ", models_gdr.best_score_)
            print("best estimator: ", models_gdr.best_estimator_)

            mlflow.log_metric(f"{model_name}_best_score",models_gdr.best_score_)
            mlflow.log_params({f"{model_name}_best_params": models_gdr.best_params_})

            if models_gdr.best_score_>best_score:
                best_score = models_gdr.best_score_
                self.best_model = models_gdr.best_estimator_
                best_model_name = model_name


        print("Best Model Type:", best_model_name)
        print("Best Model Score:", best_score)
        print("Best Model:", self.best_model)
    
    def save_model(self):
        joblib.dump(self.best_model, self.config.save_model)
        joblib.dump(self.best_model, self.config.model_for_train)