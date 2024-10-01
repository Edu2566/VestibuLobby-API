from flask import jsonify, Blueprint, url_for
import pandas as pd
import os

template_api_blueprint = Blueprint('template_api', __name__)

@template_api_blueprint.route('/template')
def get_template():
    csv_path = os.path.join(template_api_blueprint.root_path, 'static-template_api/CSV_DB/Template_DB.csv')
    db = pd.read_csv(csv_path, delimiter=';')

    data_json = db.to_dict(orient='records')

    for item in data_json:
        if 'template_pdf' in item:
            item['template_pdf_url'] = url_for('static', filename=f'pdf/{item["template_pdf"]}', _external=True)

    return jsonify(data_json)
