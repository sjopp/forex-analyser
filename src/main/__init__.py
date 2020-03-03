import requests
from pandas.io.json import json_normalize


def get_forex_data(base):
    url = 'https://api.worldtradingdata.com/api/v1/forex'
    params = {
        'base': base,
        'api_token': 'demo',
        'output': 'csv'
    }
    response = requests.request('GET', url, params=params)
    json = response.json()
    print(json)
    return json


def put_data_in_data_frame(api_response):
    data = json_normalize(api_response['data'])
    print(data)


if __name__ == '__main__':
    put_data_in_data_frame(get_forex_data("USD"))
