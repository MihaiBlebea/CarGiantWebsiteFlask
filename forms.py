from wtforms import Form, StringField, SelectField, SubmitField


class CarForm(Form):

    mpg = StringField('Mpg')
    fuel = SelectField('Select fuel type')
    mileage = StringField('Mileage')
    euro = SelectField('Standard Euro Emissions')
    transmission = SelectField('Transmission')
    submit = SubmitField('Get estimated price')


class SettingForm(Form):

    pages = StringField('How many pages to scrape (27 cars per page)')
    submit = SubmitField('Scrape and train model')
