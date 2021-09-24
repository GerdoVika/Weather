from flask import Flask, request, jsonify
import requests
from datetime import date, timedelta
import json

from config import config
from statistic import average, median


app = Flask(__name__)


def get_config() -> set:
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config['api_key'], config['api_url']


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    days = request.args.get('days')

    try:
        days = int(days)
    except ValueError:
        return jsonify({'description': 'Days must be an integer.'}), 400

    to = date.today()
    from_ = date.today() - timedelta(days=days)
    api_key, api_url = get_config()
    data = {
        'locations': city,
        'aggregateHours': 24,
        'key': api_key,
        'startDateTime': from_.__str__() + 'T00:00:00',
        'endDateTime': to.__str__() + 'T00:00:00',
        'contentType': 'json',
    }
    r = requests.get(api_url, data)

    if 'errorCode' in r.json():
        return jsonify({'description': r.json()['message']}), 400

    temperature_c = [float(item['temp']) for item in r.json()['locations'][city]['values']]
    humidity = [float(item['humidity']) for item in r.json()['locations'][city]['values']]
    pressure_mb = [float(item['sealevelpressure']) for item in r.json()['locations'][city]['values']]

    response = {
        'city': city,
        'from': from_.__str__(),
        'to': to.__str__(),
        'temperature_c': {
            'average': average(temperature_c),
            'median': median(temperature_c),
            'max': max(temperature_c),
            'min': min(temperature_c),
        },
        'humidity': {
            'average': average(humidity),
            'median': median(humidity),
            'max': round(max(humidity), 1),
            'min': round(min(humidity), 1),
        },
        'pressure_mb': {
            'average': average(pressure_mb),
            'median': median(pressure_mb),
            'max': max(pressure_mb),
            'min': min(pressure_mb),
        },
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()



