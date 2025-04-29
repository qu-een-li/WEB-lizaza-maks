from flask import Blueprint, jsonify

regions_api = Blueprint('regions_api', __name__)

REGION_ID = 1086244

def get_regions_data():
    return [{"id": REGION_ID,
             "title": "Республика Северная Осетия — Алания"
    }]

@regions_api.route('/api/regions', methods=['GET'])
def get_regions():
    return jsonify(get_regions_data())