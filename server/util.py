import pickle
import json
import numpy as np

__fuel_type = None
__owner_type = None
__transmission = None
__name = None
__data_columns = None
__model = None


def get_car_price(Name, Year, Kilometers_Drive, Seats, Engine_n, Power_n, Mileage_n, Fuel_type, Transmission,
                  Owner_type):
    try:
        fuel_type_index = __data_columns.index(Fuel_type.lower())
        transmission_index = __data_columns.index(Transmission.lower())
        owner_type_index = __data_columns.index(Owner_type.lower())
        name_index = __data_columns.index(Name.lower())
    except:
        fuel_type_index = -1
        transmission_index = -1
        owner_type_index = -1
        name_index = -1


    x1 = np.zeros(len(__data_columns))
    x1[0] = Year
    x1[1] = Kilometers_Drive
    x1[2] = Seats
    x1[3] = Engine_n
    x1[4] = Power_n
    x1[5] = Mileage_n
    if fuel_type_index >= 0:
        x1[fuel_type_index] = 1
    if transmission_index >= 0:
        x1[transmission_index] = 1
    if owner_type_index >= 0:
        x1[owner_type_index] = 1
    if name_index >= 0:
        x1[name_index] = 1

    return round(__model.predict(x1)[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __fuel_type
    global __owner_type
    global __transmission
    global __name


    with open("./artifacts/columns_car.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __fuel_type = __data_columns[6:10]
        __transmission = __data_columns[10:12]
        __owner_type = __data_columns[12:16]
        __name = __data_columns[16:]

    global __model
    if __model is None:
        with open('./artifacts/used_car_price_prediction_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")


def get_fuel_type_names():
    return __fuel_type


def get_owner_type_names():
    return __owner_type


def get_transmission_names():
    return __transmission


def get_name_names():
    return __name


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_fuel_type_names())
    print(get_owner_type_names())
    print(get_transmission_names())
    print(get_name_names())

    print(get_car_price('Maruti Wagon R LXI CNG', 2010, 72000, 5, 998, 58.16, 26.60, 'CNG', 'Manual', 'First'))
    print(get_car_price('Maruti Wagon R LXI CNG', 2010, 52000, 6, 998, 38.16, 26.60, 'CNG', 'Manual', 'First'))
    print(get_car_price('Audi A4 New 2.0 TDI Multitronic', 2010, 72000, 5, 998, 58.16, 26.60, 'Diesel', 'Automatic',
                    'Second'))