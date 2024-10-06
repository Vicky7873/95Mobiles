from flask import Flask,render_template,Blueprint,request
from sklearn.preprocessing import LabelEncoder,StandardScaler
from log import logger
import joblib
import pandas as pd

mobile_app  = Blueprint('mobile_app',__name__,template_folder='/Users/bhikipallai/Desktop/Projects/95Mobiles/templates')

model_predict = joblib.load("models/mobile.pkl")

le = LabelEncoder()
stc = StandardScaler()

@mobile_app.route('/')
def index():
    return render_template('mobile_index.html')


@mobile_app.route('/predict',methods = ["GET","POST"])
def predict():
    if request.method == "POST":
        brand = request.form["brand"]
        model = request.form["model"]
        storage = request.form["storage"]
        ram = request.form["ram"]
        screen_size = request.form["screen_size"]
        camera = request.form["camera"]
        battery = int(request.form["battery"])

        df = pd.DataFrame({
            "Brand": [brand],
            "Model": [model],
            "Storage": [storage],
            "RAM": [ram],
            "screen_size": [screen_size],
            "camera": [camera],
            "battery": [battery]
        })

        cat_cols = []
        num_cols = []
        for col in df.columns:
            if df[col].dtype == 'object':
                cat_cols.append(col)
            else:
                num_cols.append(col)

        print(cat_cols)
        print(num_cols)

        for col in df[cat_cols]:
            df[col] = le.fit_transform(df[[col]])
        df[num_cols] = stc.fit_transform(df[num_cols])

        result = model_predict.predict(df)

    return render_template('mobile_result.html',predicted_price = result)