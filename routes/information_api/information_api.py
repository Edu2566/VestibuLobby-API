from flask import jsonify, Blueprint
import pandas as pd
import os

information_api_blueprint = Blueprint('information_api', __name__)

@information_api_blueprint.route('/information')
def get_information():

  csv_path = os.path.join(information_api_blueprint.root_path, 'static-information_api/CSV_DB/Information_DB.csv')
  db = pd.read_csv(csv_path, delimiter=';')

  data_json = db.to_dict(orient='records')

  return jsonify(data_json)