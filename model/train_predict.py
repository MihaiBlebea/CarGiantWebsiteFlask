from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

from pandas import Series, DataFrame
import numpy as np


def split_train_test(df_features, df_labels):
    return train_test_split(df_features, df_labels, test_size=0.2, shuffle=True, random_state=0)


def train_model(df_features, df_labels):
    lr = LinearRegression()
    # lr = LogisticRegression()
    model = lr.fit(df_features, df_labels)
    return model


def predict_result(model, df_features):
    prediction = model.predict(df_features)
    return Series(np.array(prediction).astype(int))
