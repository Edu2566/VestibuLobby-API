from flask import jsonify, Blueprint
import pandas as pd
import os

course_api_blueprint = Blueprint('course_api', __name__)

@course_api_blueprint.route('/courses')
def get_course():

    csv_path = os.path.join(course_api_blueprint.root_path, 'static-course_api/CSV_DB/Course_DB.csv')
    db = pd.read_csv(csv_path, delimiter=';')

    data_json = db.to_dict(orient='records')

    return jsonify(data_json)