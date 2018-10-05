

class ProcessData:

    def __init__(self, data, feature_columns, label):
        self.data = data
        self.feature_columns = feature_columns
        self.label = label


    def remove_missing(self):
        columns = self.feature_columns + [ self.label ]
        return self.data[columns].dropna()
