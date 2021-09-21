from flask import Flask, request, jsonify
import requests
import pandas as pd
import numpy as np
from datetime import date, timedelta
from config import config


app = Flask(__name__)


def get_api_key() -> str:
    return config['api_key']


def get_metrics(data: pd.Series) -> dict:
  data = data.to_numpy()
  metrics = {
      'average': np.around(np.average(data), decimals=1),
      'median': np.around(np.median(data), decimals=1),
      'max': np.around(np.max(data), decimals=1),
      'min': np.around(np.min(data), decimals=1),
  }
  return metrics


@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    days = request.args.get('days')
    url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/weatherdata/history'

    try:
        days = int(days)
    except ValueError:
        return jsonify({'description': 'Days must be an integer.'}), 400

    to = date.today()
    from_ = date.today() - timedelta(days=days)
    data = {
        'locations': city,
        'aggregateHours': 24,
        'key': get_api_key(),
        'startDateTime': from_.__str__() + 'T00:00:00',
        'endDateTime': to.__str__() + 'T00:00:00',
        'contentType': 'json',
    }
    r = requests.get(url, data)

    if 'errorCode' in r.json():
        return jsonify({'description': r.json()['message']}), 400

    data = pd.DataFrame.from_records(r.json()['locations'][city]['values'])
    response = {
        'city': city,
        'from': from_.__str__(),
        'to': to.__str__(),
        'temperature_c': get_metrics(data['temp']),
        'humidity': get_metrics(data['humidity']),
        'pressure_mb': get_metrics(data['sealevelpressure']),
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()



