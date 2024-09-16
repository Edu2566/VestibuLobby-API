from flask import jsonify, Blueprint
import pandas as pd
import os

location_api_blueprint = Blueprint('location_api', __name__)

@location_api_blueprint.route('/location')
def get_location():

  csv_path = os.path.join(location_api_blueprint.root_path, 'static-location_api/CSV_DB/Location_DB.csv')
  db = pd.read_csv(csv_path, delimiter=';')

  data_json = db.to_dict(orient='records')

  return jsonify(data_json)