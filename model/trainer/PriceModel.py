from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from pandas import Series


class PriceModel:

    def __init__(self):
        pass

    def train_mode(self):
        pass

    def predict(self):
        pass


class LinearRegressionModel(PriceModel):

    def __init__(self, features, label):
        self.x_train, self.y_train, self.x_test, self.y_test = train_test_split(features, label, test_size=0.2, shuffle=True, random_state=0)


    def train_model(self):
        lr = LinearRegression()
        return lr.fit(self.x_train, self.y_train)


    def predict(self, model, x_predict):
        prediction = model.predict(x_predict)
        return Series(np.array(prediction).astype(int))
