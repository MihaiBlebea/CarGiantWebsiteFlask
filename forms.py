from wtforms import Form, StringField, SelectField, SubmitField


class CarForm(Form):

    brand = SelectField('Select car model')
    body = SelectField('Select body type')
    engine = StringField('Engine size')
    fuel = SelectField('Select fuel type', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    acceleration = StringField('Acceleration')
    submit = SubmitField('Get estimated price')
