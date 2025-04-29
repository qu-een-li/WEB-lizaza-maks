from flask import Blueprint, jsonify
import requests

cities_api = Blueprint('cities_api', __name__)

SERVICE_KEY = "b23f635fb23f635fb23f635f26b110e9c3bb23fb23f635fda3f614c627d359f88d1a62e"
API_VERSION = '5.199'

def get_cities_data(region_id):
    url = 'https://api.vk.com/method/database.getCities'
    params = {
        'access_token': SERVICE_KEY,
        'v': API_VERSION,
        'region_id': region_id,
        'need_all': 1,
        'lang': 'ru',
        'count': 1000,
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if 'response' in data and 'items' in data['response']:
            return [{'id': city['id'], 'title': city['title']} for city in data['response']['items']]
        return []
    except Exception as e:
        print(f"Ошибка при выборе городов: {e}")
        return []

@cities_api.route('/api/cities/<int:region_id>', methods=['GET'])
def get_cities(region_id):
    return jsonify(get_cities_data(region_id))