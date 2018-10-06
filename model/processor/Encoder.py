from sklearn.preprocessing import LabelEncoder


class Encoder:

    def train(self, data):
        pass

    def encode(self, encoder):
        pass


    def check_columns(self, data, columns):
        string_columns = []
        for column in columns:
            if self.check_integer(data[column][0]) is False and self.check_float(data[column][0]) is False:
                string_columns.append(column)
        return string_columns


    def check_integer(self, value):
        try:
            int(value)
            return True
        except ValueError:
            return False


    def check_float(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False


    def get_string_columns(self, data):
        columns = list(data.columns.values)
        return self.check_columns(data, columns)


class EncodeLabel(Encoder):

    def train(self, data):
        string_columns = self.get_string_columns(data)
        encoder = LabelEncoder()
        for column in string_columns:
            encoder.fit_transform(data[column])
        return encoder


    def encode(self, data, encoder):
        string_columns = self.get_string_columns(data)
        for column in string_columns:
            encoded_labels = encoder.fit_transform(data[column])
            data[column] = encoded_labels
        return data
