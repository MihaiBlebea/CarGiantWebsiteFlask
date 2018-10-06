from model.scraper import ScraperFacade
from model.processor import ProcessData, EncodeLabel, Object, Excel
from model.trainer import LinearRegressionModel


class CreateModelFacade:

    def __init__(self, url, feature_columns, label_column, max_page = 2):
        self.url = url
        self.feature_columns = feature_columns
        self.label_column = label_column
        self.max_page = max_page


    def get_data(self):
        scraper = ScraperFacade(self.url, self.max_page)
        data = scraper.get_formated_data()

        data_excel = Excel('data/excel_data.xlsx')
        data_excel.save(data)

        return data


    def get_features_labels(self):
        data = self.get_data()

        process_data = ProcessData(data, self.feature_columns, self.label_column)
        df_features, df_label = process_data.prepare_data()

        encoder = EncodeLabel()
        encoder_model = encoder.train(df_features)
        encoded_features = encoder.encode(df_features, encoder_model)

        encode_model_object = Object('data/encode_model.model')
        encode_model_object.save(encoder_model)

        return encoded_features, df_label


    def get_model(self):
        predict_model_object = Object('data/predict_model.model')

        df_features, df_labels = self.get_features_labels()
        lr_model = LinearRegressionModel(df_features, df_labels)
        model = lr_model.train_model()
        predict_model_object.save(model)

        return model
