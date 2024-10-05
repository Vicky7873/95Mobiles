from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import ElasticNet,Ridge,Lasso
import mlflow
import joblib
import pandas as pd
import dagshub
from sklearn.model_selection import GridSearchCV
from src.laptop.entity import ModelTrainingConfig



models = {
    "lr":LinearRegression(),
    "rfr":RandomForestRegressor(),
    "dtr":DecisionTreeRegressor(),
    "enet":ElasticNet(),
    "ridge":Ridge(),
    "lasso":Lasso()
}


grid_params = {
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
    },
    "enet":{
        "alpha":[1.0,0.5,1.5,2.0],
        "l1_ratio" :[0.3,0.4,0.5],
        "selection": ["cyclic","random"]
    },
    "ridge":{
        "alpha":[1.0,0.5,1.5,2.0],
        "solver":['auto', 'svd', 'cholesky', 'lsqr', 'sparse_cg', 'sag', 'saga']
    },

    "lasso" : {
        "alpha":[1.0,0.5,1.5,2.0],
    }
}



class Laptop_modeltrain:
    def __init__(self,config:ModelTrainingConfig):
        self.config = config
    
    def model_train(self):
        X_train = pd.read_csv(self.config.X_train)
        X_test = pd.read_csv(self.config.X_test)
        y_train = pd.read_csv(self.config.y_train)
        y_test = pd.read_csv(self.config.y_test)

        dagshub.init(repo_owner='Vicky7873', repo_name='95Mobiles', mlflow=True)
        mlflow.set_registry_uri("https://dagshub.com/Vicky7873/95Mobiles.mlflow")
        mlflow.set_experiment("Laptop model training")

        compare_score = -float("inf")
        with mlflow.start_run():
            for model_name,model in models.items():
                train_gdr = GridSearchCV(model,param_grid=grid_params[model_name],cv=5)
                train_gdr.fit(X_train,y_train)
                print("Best parameters: ", train_gdr.best_params_)
                print("best score: ", train_gdr.best_score_)
                print("best estimator: ", train_gdr.best_estimator_)

                mlflow.log_metric(f"{model_name}_best_score",train_gdr.best_score_)
                mlflow.log_params({f"{model_name}_best_params": train_gdr.best_params_})

                if train_gdr.best_score_>compare_score:
                    compare_score = train_gdr.best_score_
                    self.best_model = train_gdr.best_estimator_
                    print("Best Model Type:", self.best_model)
    

    def model_save(self):
        model = self.best_model
        joblib.dump(model,self.config.saved_model)
        joblib.dump(model, self.config.model_for_train)
        print(f"Model: {model} was saved to its path")
