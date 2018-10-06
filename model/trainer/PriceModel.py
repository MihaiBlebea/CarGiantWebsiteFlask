from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from pandas import Series
import numpy as np


class PriceModel:

    def __init__(self):
        pass

    def train_mode(self):
        pass

    def predict(self):
        pass


class LinearRegressionModel(PriceModel):

    def __init__(self, features, label):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(features, label, test_size=0.2, shuffle=True, random_state=0)
        self.model = None


    def train_model(self):
        linear_r = LinearRegression()
        self.model = linear_r.fit(self.x_train, self.y_train)
        return self.model


    def predict(self, x_predict, model = None):
        if model is None:
            if self.model is not None:
                model = self.model
            else:
                raise Exception('Model is not trained yet. Please provide model or run "train_model" method')

        prediction = model.predict(x_predict)
        return Series(np.array(prediction).astype(int))
