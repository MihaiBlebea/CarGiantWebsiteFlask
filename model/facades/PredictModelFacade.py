from model.processor import Object, EncodeLabel


class PredictModelFacade:

    def __init__(self, encoder_path, model_path):
        self.encoder_path = encoder_path
        self.model_path = model_path


    def encode(self, data):
        encoder_obj = Object(self.encoder_path)
        encoder_model = encoder_obj.load()
        encoder = EncodeLabel()
        return encoder.encode(data, encoder_model)


    def predict(self, data):
        encoded_data = self.encode(data)

        model_obj = Object(self.model_path)
        model = model_obj.load()

        return int(model.predict(encoded_data))
