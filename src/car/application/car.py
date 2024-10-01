from flask import Flask,render_template,Blueprint,request
from sklearn.preprocessing import StandardScaler,LabelEncoder
from log import logger
import joblib
import pandas as pd

car_app = Blueprint("car_app",__name__,template_folder="/Users/bhikipallai/Desktop/Projects/95Mobiles/templates")

model = joblib.load("models/car_best_model.pkl")

le = LabelEncoder()
stc = StandardScaler()


@car_app.route('/')
def index():
    return render_template("car_index.html")

@car_app.route('/predict',methods = ["GET","POST"])
def car_predict():
    if request.method == "POST":
        name = request.form["name"]
        year = request.form["year"]
        km_driven = float(request.form['km_driven'])
        fuel = request.form["fuel"]
        seller_type = request.form["seller_type"]
        transmission = request.form["transmission"]
        owner = request.form["owner"]

        df = pd.DataFrame({
            "name":[name],
            "year":[year],
            "km_driven":[km_driven],
            "fuel":[fuel],
            "seller_type":[seller_type],
            "transmission":[transmission],
            "owner":[owner]
        })

        stc = StandardScaler()
        df[['year', 'km_driven']] = stc.fit_transform(df[['year', 'km_driven']])

        cat_cols = ['name', 'fuel', 'seller_type', 'transmission', 'owner']
        for col in cat_cols:
            df[col] = le.fit_transform(df[col])

        result = model.predict(df)

    return render_template("car_result.html", predicted_price = result)