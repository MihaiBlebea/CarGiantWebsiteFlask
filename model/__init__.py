from model.scraper_data import retrive_data
from model.process_data import get_features, get_labels, encode_labels, train_encoder, drop_missing, save_excel, load_excel, save_obj, load_obj
from model.train_predict import train_model, predict_result, split_train_test

from pathlib import Path
import pandas as pd


def get_column_uniq_variants(excel_file_path, column_name):
    excel_file = Path(excel_file_path)
    if excel_file.exists():
        df_data = load_excel(excel_file_path)
        return df_data[column_name].unique()
    else:
        raise Exception('Can\'t find data excel file with scraped data')


def get_data(root_url, max_pages, excel_file_path):
    excel_file = Path(excel_file_path)
    if excel_file.exists():
        df_data = load_excel(excel_file_path)
    else:
        df_data = retrive_data(root_url, max_pages)
        save_excel(excel_file_path, df_data)

    return df_data


def process_data(df_data, feature_columns, label_column):
    columns = feature_columns + [label_column]
    df_data = drop_missing(df_data, columns)
    df_features = get_features(df_data, feature_columns)
    df_labels = get_labels(df_data, label_column)

    return df_features, df_labels


# x_train, x_test, y_train, y_test = split_train_test(df_features, df_labels)


def get_model(model_file_path, df_features, df_labels):
    model_file = Path(model_file_path)
    if model_file.exists():
        model = load_obj(model_file_path)
    else:
        model = train_model(df_features, df_labels)
        save_obj(model, model_file_path)

    return model
