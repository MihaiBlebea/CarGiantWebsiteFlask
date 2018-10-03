from flask import Flask, request, render_template
from forms import CarForm
import pandas as pd
from pandas import DataFrame

from model import get_column_uniq_variants, get_data, process_data, get_model, predict_result, train_encoder, encode_labels


app = Flask(__name__)


def parse_input_select_data(data_path, column_name):
    uniq_data = get_column_uniq_variants(data_path, column_name)
    result = [('', 'Please select an option')]
    for option in uniq_data:
        result.append((option, option))
    return result


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    form = CarForm()

    form.fuel.choices = parse_input_select_data('data/excel_data.xlsx', 'Fuel')
    form.euro.choices = parse_input_select_data('data/excel_data.xlsx', 'Standard Euro Emissions')
    form.transmission.choices = parse_input_select_data('data/excel_data.xlsx', 'Transmission')


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

        feature_columns = ['EC Combined (mpg)', 'Fuel', 'Mileage', 'Standard Euro Emissions', 'Transmission']
        label_column = 'Price'

        data = get_data('https://www.cargiant.co.uk/search', 2, 'data/excel_data.xlsx')
        df_features, df_labels = process_data(data, feature_columns, label_column)

        encoder = train_encoder(df_features)
        df_features = encode_labels(df_features, encoder)
        encoded_input = encode_labels(df_input, encoder)

        model = get_model('data/predict_price.model', df_features, df_labels)

        prediction = predict_result(model, encoded_input)
        print(prediction)

        return render_template('pages/landing.html', form = form, result = True, price = prediction[0])
    else:
        return render_template('pages/landing.html', form = form)


if __name__ == '__main__':
    app.run(debug = True)
