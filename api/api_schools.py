from flask import Blueprint, jsonify
import requests

schools_api = Blueprint('schools_api', __name__)

SERVICE_KEY = "b23f635fb23f635fb23f635f26b110e9c3bb23fb23f635fda3f614c627d359f88d1a62e"
API_VERSION = '5.199'

def get_schools_data(city_id):
    url = 'https://api.vk.com/method/database.getSchools'
    params = {
        'access_token': SERVICE_KEY,
        'v': API_VERSION,
        'city_id': city_id,
        'count': 1000,
        'lang': 'ru'
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        if 'response' in data and 'items' in data['response']:
            return [{'id': school['id'], 'title': school['title']} for school in data['response']['items']]
        return []
    except Exception as e:
        print(f"Ошибка при выборе школ: {e}")
        return []

@schools_api.route('/api/schools/<int:city_id>', methods=['GET'])
def get_schools(city_id):
    return jsonify(get_schools_data(city_id))