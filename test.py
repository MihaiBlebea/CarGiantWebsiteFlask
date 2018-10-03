from model import get_column_uniq_variants, get_data, process_data, train_model, predict_result, encode_labels, train_encoder

feature_columns = ['EC Combined (mpg)', 'Fuel', 'Mileage', 'Standard Euro Emissions', 'Transmission']
label_column = 'Price'


data = get_data('https://www.cargiant.co.uk/search', 3, 'data/excel_data.xlsx')

df_features, df_labels = process_data(data, feature_columns, label_column)
encoder = train_encoder(df_features)
df_features = encode_labels(df_features, encoder)
# model = train_model('data/predict_price.model', df_features, df_labels)
print(df_features)

# prediction = predict_result(model, df_features)
# print('score is ' + str(model.score()))
# print(prediction)
