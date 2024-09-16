from flask import jsonify, Blueprint, url_for
import pandas as pd
import os

exams_api_blueprint = Blueprint('exams_api', __name__)

@exams_api_blueprint.route('/exams')
def get_exams():
    # Caminho para o arquivo CSV
    csv_path = os.path.join(exams_api_blueprint.root_path, 'static-exams_api/CSV_DB/Exams_DB.csv')
    # Ler o CSV usando pandas
    db = pd.read_csv(csv_path, delimiter=';')

    # Converter DataFrame para lista de dicionários
    data_json = db.to_dict(orient='records')

    # Adicionar URL base para os PDFs
    for item in data_json:
        if 'exam_pdf' in item:
            # Montar a URL completa para o PDF
            item['exam_pdf_url'] = url_for('static', filename=f'pdf/{item["exam_pdf"]}', _external=True)

    return jsonify(data_json)
