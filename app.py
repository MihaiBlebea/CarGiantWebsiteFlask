from flask import Flask, request, render_template
from forms import CarForm
from cg_predict_price import CGData, CGPredict, CGEncode
import pandas as pd
from pandas import DataFrame

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    form = CarForm()

    form.brand.choices = [('Fiat Panda', 'Fiat Panda'), ('Smart Fortwo', 'Smart Fortwo'), ('Ford Ka', 'Ford Ka')]
    form.body.choices = [('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Cabriolet', 'Cabriolet')]
    form.fuel.choices = [('Petrol', 'Petrol')]

    if request.method == 'POST':

        brand = request.form['brand']
        body = request.form['body']
        engine = request.form['engine']
        fuel = request.form['fuel']
        acceleration = request.form['acceleration']

        df = pd.DataFrame({
            "Body Type": [body],
            "Engine size": [engine],
            "0 to 62 mph (secs)": [acceleration],
            "Fuel": [fuel],
            "Car": [brand]
        })

        cg_encode = CGEncode('data/encode_dict.json')
        labels = ['Body Type', 'Engine size', 'Fuel', '0 to 62 mph (secs)', 'Car']

        df = cg_encode.encode_to_integer(df, labels)

        cg_data = CGData('https://www.cargiant.co.uk/search', labels, 'Price', cg_encode, max_pages = 4)
        cg_data.load_or_scrape_data('data/car_data.xlsx')
        df_features = cg_data.get_features()
        df_labels = cg_data.get_labels()

        cg_predict = CGPredict(df_features, df_labels)
        cg_predict.train_or_load('data/car_price.model')
        prediction = cg_predict.predict(df)

        score = cg_predict.get_score()

        brand = request.form['brand']

        return render_template('pages/landing.html', form = form, result = True, score = score, price = prediction[0], brand = brand)
    else:
        return render_template('pages/landing.html', form = form)


if __name__ == '__main__':
    app.run(debug = True)
