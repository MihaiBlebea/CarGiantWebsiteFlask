from pandas import ExcelWriter, read_excel
import pickle
from pathlib import Path


class Persist:

    def __init__(self):
        pass

    def save(self, data):
        pass

    def load(self):
        pass

    def get_if_exists(self, callback):
        print('RUN FUNCTION "get if exists"')
        file = Path(self.path)
        if file.exists():
            data = self.load()
        else:
            data = callback()
            self.save(data)

        return data


class Excel(Persist):

    def __init__(self, path):
        self.path = path


    def save(self, data, sheet = 'Sheet1'):
        writer = ExcelWriter(self.path)
        data.to_excel(writer, sheet, index = False)
        writer.save()


    def load(self, sheet = 'Sheet1'):
        return read_excel(self.path, sheet_name=sheet)


class Object(Persist):

    def __init__(self, path):
        self.path = path


    def save(self, data):
        pickle.dump(data, open(self.path, 'wb'))


    def load(self):
        return pickle.load(open(self.path, 'rb'))
