from flask import Flask, request, render_template
from forms.CarForm import CarForm
import cg_predict_price.app
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    form = CarForm()

    form.brand.choices = [('cpp', 'Hatchback'), ('py', 'Python'), ('text', 'Plain Text')]
    form.body.choices = [('cpp', 'Hatchback'), ('py', 'Python'), ('text', 'Plain Text')]

    if request.method == 'POST':
        brand = request.form['brand']

        return render_template('pages/landing.html', form = form, result = True)
    else:
        return render_template('pages/landing.html', form = form)


if __name__ == '__main__':
    app.run(debug = True)
