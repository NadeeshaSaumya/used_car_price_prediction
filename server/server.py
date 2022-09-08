from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_fuel_type_names', methods=['GET'])
def get_fuel_type_names():
    response = jsonify({
        'Fuel_type': util.get_fuel_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_owner_type_names', methods=['GET'])
def get_owner_type_names():
    response = jsonify({
        'Owner_type': util.get_owner_type_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_transmission_names', methods=['GET'])
def get_transmission_names():
    response = jsonify({
        'Transmission': util.get_transmission_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_name_names', methods=['GET'])
def get_name_names():
    response = jsonify({
        'Name': util.get_name_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_used_car_price', methods=['GET', 'POST'])
def predict_used_car_price():
    Seats = float(request.form['Seats'])
    Power_n = float(request.form['Power'])
    Mileage_n = float(request.form['Mileage'])


    Year = int(request.form['Year'])
    Kilometers_Drive = int(request.form['Kilometers_Drive'])
    Engine_n = int(request.form['Engine'])
    Name = request.form['Name']
    Fuel_type = request.form['Fuel_type']
    Transmission = request.form['Transmission']
    Owner_type = request.form['Owner_type']

    response = jsonify({
        'estimated_price': util.get_car_price(Name, Year, Kilometers_Drive, Seats, Engine_n, Power_n, Mileage_n, Fuel_type,
                                              Transmission, Owner_type)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Used Car Price Prediction...")
    util.load_saved_artifacts()
    app.run()