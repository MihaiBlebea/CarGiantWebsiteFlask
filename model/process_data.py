import pandas as pd
import numpy as np
from pandas import ExcelWriter, Series
import pickle
from sklearn.preprocessing import LabelEncoder
# from collections import defaultdict


def create_encode_dict(df, columns):
    encode_dict = {}
    for column in columns:
        df_no_dupli = df.drop_duplicates(column)
        df_no_dupli_indexed = df_no_dupli.assign(encode_values_int = Series( np.arange( 1, len(df_no_dupli.index) + 1 )).values )
        df_two_columns = df_no_dupli_indexed[[column, 'encode_values_int']]

        d = {}
        for index, row in df_two_columns.iterrows():
            d[row[column]] = row['encode_values_int']

        encode_dict[column] = d
    return encode_dict


# Encode the items in the Data Frame using the dict
def encode_to_integer(df, columns):
    string_columns = check_columns(df, columns)
    encode_dict = create_encode_dict(df, columns)

    for column in string_columns:
        for index, row in df.iterrows():
            df.loc[index, column] = encode_dict[column][row[column]]

    return df


def train_encoder(df):
    string_columns = get_string_columns(df)
    encoder = LabelEncoder()
    for column in string_columns:
        encoder.fit_transform(df[column])
    return encoder


def encode_labels(df, encoder):
    string_columns = get_string_columns(df)
    for column in string_columns:
        encoded_labels = encoder.fit_transform(df[column])
        df[column] = encoded_labels
    return df


def get_string_columns(df):
    columns = list(df.columns.values)
    return check_columns(df, columns)

# def encode_labels(df):
#     columns = list(df.columns.values)
#     string_columns = check_columns(df, columns)
#     encoder = LabelEncoder()
#     for column in string_columns:
#         encoded_labels = encoder.fit_transform(df[column])
#         df[column] = encoded_labels
#     return df


def encode_to_dummy(df):
    columns = list(df.columns.values)
    string_columns = check_columns(df, columns)

    for column in string_columns:
        col_uniq_values = df[column].unique()
        dict = {}
        dict.fromkeys(range(0, len(col_uniq_values)), col_uniq_values)

        df[column] = df[column].replace(dict)
        df = pd.get_dummies(df, columns=[column])
    return df


def drop_missing(df, columns):
    return df[columns].dropna()


def check_columns(df, columns):
    string_columns = []
    for column in columns:
        if check_integer(df[column][0]) is False and check_float(df[column][0]) is False:
            string_columns.append(column)
    return string_columns


def check_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def check_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_features(df_data, feature_columns):
    df_features = df_data[feature_columns]
    return df_features
    # return encode_to_integer(df_features, feature_columns)


def get_labels(df_data, label):
    return df_data[label]


def save_excel(file_name, data):
    writer = ExcelWriter(file_name)
    data.to_excel(writer, 'Sheet1', index = False)
    writer.save()


def load_excel(file_name):
    return pd.read_excel(file_name, sheet_name='Sheet1')


def save_obj(obj, file_path):
    pickle.dump(obj, open(file_path, 'wb'))


def load_obj(file_path):
    return pickle.load(open(file_path, 'rb'))
