

class Format:

    def execute(self, data):
        pass


class RemoveMoneySign(Format):

    def execute(self, data):
        for column in data:
            if '£' in data[column]:
                data[column] = data[column].replace('£', '')
        return data


class RemoveAsterix(Format):

    def execute(self, data):
        for column in data:
            if '*' in data[column]:
                data[column] = data[column].replace('*', '').strip()
        return data


class RemoveComma(Format):

    def execute(self, data):
        for column in data:
            if ',' in data[column]:
                data[column] = data[column].replace(',', '')
        return data


class DataFormater:

    def __init__(self, data):
        self.formats = []
        self.data = data


    def add(self, format):
        self.formats.append(format)


    def run(self):
        for format in self.formats:
            self.data = format.execute(self.data)

        return self.data


# How to implement Data Formater
data_formater = DataFormater(data)
data_formater.add( RemoveMoneySign() )
data_formater.add( RemoveAsterix() )
data_formater.add( RemoveComma() )
data = data_formater.run()
