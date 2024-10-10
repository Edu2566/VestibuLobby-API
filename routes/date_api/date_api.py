from flask import jsonify, Blueprint
import pandas as pd
import os

date_api_blueprint = Blueprint('date_api', __name__)

@date_api_blueprint.route('/date')
def get_date():

  csv_path = os.path.join(date_api_blueprint.root_path, 'static-date_api/CSV_DB/Date_DB.csv')
  db = pd.read_csv(csv_path, delimiter=';')

  data_json = db.to_dict(orient='records')

  return jsonify(data_json)