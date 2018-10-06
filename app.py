from flask import Flask, request, render_template, redirect
from forms import CarForm, SettingForm
import pandas as pd
from pandas import DataFrame
import os

from model import CreateModelFacade, PredictModelFacade, Excel

# from model import get_column_uniq_variants, get_data, process_data, get_model, predict_result, train_encoder, encode_labels


app = Flask(__name__)

feature_columns = ['EC Combined (mpg)', 'Fuel', 'Mileage', 'Standard Euro Emissions', 'Transmission']
label_column = 'Price'


def parse_input_select_data(column_name):
    uniq_data = get_column_uniq_variants(column_name)
    result = [('', 'Please select an option')]
    for option in uniq_data:
        result.append((option, option))
    return result


def get_column_uniq_variants(column_name):
    excel = Excel('data/excel_data.xlsx')
    data = excel.load()
    return data[column_name].unique()


@app.route('/help', methods = ['GET'])
def help():
    return render_template('pages/help.html')


@app.route('/about', methods = ['GET'])
def about():
    return render_template('pages/about.html')


@app.route('/', methods = ['GET', 'POST'])
def homepage():

    form = CarForm()

    form.fuel.choices = parse_input_select_data('Fuel')
    form.euro.choices = parse_input_select_data('Standard Euro Emissions')
    form.transmission.choices = parse_input_select_data('Transmission')


    if request.method == 'POST':

        mpg = request.form['mpg']
        fuel = request.form['fuel']
        mileage = request.form['mileage']
        euro = request.form['euro']
        transmission = request.form['transmission']

        if fuel == '' or euro == '' or transmission == '':
            return render_template('pages/landing.html', form = form, result = False, field_error = True)

        df_input = pd.DataFrame({
            'EC Combined (mpg)': [mpg],
            'Fuel': [fuel],
            'Mileage': [mileage],
            'Standard Euro Emissions': [euro],
            'Transmission': [transmission]
        })

        predict_model_facade = PredictModelFacade('data/encode_model.model', 'data/predict_model.model')
        prediction = predict_model_facade.predict(df_input)

        return render_template('pages/landing.html', form = form, result = True, price = prediction)
    else:
        return render_template('pages/landing.html', form = form)


if __name__ == '__main__':
    app.run(debug = True)
