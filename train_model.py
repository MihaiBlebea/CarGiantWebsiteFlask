from model import CreateModelFacade


feature_columns = ['EC Combined (mpg)', 'Fuel', 'Mileage', 'Standard Euro Emissions', 'Transmission']
label_column = 'Price'

create_model_facade = CreateModelFacade('https://www.cargiant.co.uk', feature_columns, label_column, 2)
model = create_model_facade.get_model()
