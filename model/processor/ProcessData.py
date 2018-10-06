

class ProcessData:

    def __init__(self, data, feature_columns, label_column):
        self.data = data
        self.feature_columns = feature_columns
        self.label_column = label_column


    def prepare_data(self):
        self.data = self.remove_missing()
        df_features = self.get_features()
        df_label = self.get_labels()
        return df_features, df_label


    def remove_missing(self):
        columns = self.feature_columns + [ self.label_column ]
        return self.data[columns].dropna()


    def get_features(self):
        return self.data[self.feature_columns]


    def get_labels(self):
        return self.data[self.label_column]
