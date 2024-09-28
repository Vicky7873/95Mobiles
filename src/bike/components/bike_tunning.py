from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge,Lasso,ElasticNet
from sklearn.model_selection import GridSearchCV
import pandas as pd
import mlflow
import joblib
import dagshub
from src.bike.entity import BikeModelTuningConfig

models = {
    "lr":LinearRegression(),
    "rfr":RandomForestRegressor(),
    "dtr":DecisionTreeRegressor(),
    "ridge":Ridge(),
    "lasso":Lasso(),
    "enet":ElasticNet()
}

grid_params = {
    "lr" : {
        "fit_intercept":[False,True]
        # "positive":[False,True]
    },

    "rfr" : {
        "n_estimators":[1,2,3],
        "criterion": ["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "bootstrap" : [True,False],
        "oob_score" : [True,False]
    },

    "dtr" : {
        "criterion": ["squared_error", "absolute_error", "friedman_mse", "poisson"],
        "splitter":["best","random"],
    },

    "ridge":{
        "alpha":[1.0,0.5,1.5,2.0],
        "solver":['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']
    },

    "lasso" : {
        "alpha":[1.0,0.5,1.5,2.0],
    },

    "enet" : {
        "alpha":[1.0,0.5,1.5,2.0],
        "l1_ratio" :[0.3,0.4,0.5],
        "selection": ["cyclic","random"]
    }
}


class BikeTunning:
    def __init__(self,config:BikeModelTuningConfig):
        self.config = config
        self.best_score = -float('inf')
    
    def tunned_model(self):
        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        X_train = pd.read_csv(self.config.X_train)
        y_train = pd.read_csv(self.config.y_train)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        mlflow.set_experiment('Bike_model_training')
        with mlflow.start_run():
            for model_name, model in models.items():
                train = GridSearchCV(model,param_grid=grid_params[model_name],cv=5)
                train.fit(X_train,y_train)
                mlflow.log_metric(f"{model_name}_best_score", train.best_score_)
                mlflow.log_params({f"{model_name}_best_params": train.best_params_})
                best_score = train.best_score_

                if best_score>self.best_score:
                    self.best_score = best_score
                    joblib.dump(train.best_estimator_,self.config.tunned_model)
                    print("Best Model Type:", type(train.best_estimator_,).__name__)

        # return best_model