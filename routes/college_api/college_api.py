from flask import jsonify, send_from_directory, Blueprint, url_for
import pandas as pd
import os

college_api_blueprint = Blueprint('college_api', __name__)

# Diretório onde as imagens estão armazenadas
image_folder = os.path.join(college_api_blueprint.root_path)

@college_api_blueprint.route('/')
def get_colleges():
    # Caminho para o arquivo CSV
    csv_path = os.path.join(college_api_blueprint.root_path, 'static-college_api/CSV_DB/College_DB.csv')
    # Ler o CSV usando pandas
    db = pd.read_csv(csv_path, delimiter=';')

    # Converter DataFrame para lista de dicionários
    data_json = db.to_dict(orient='records')

    # Adicionar URL base para as imagens
    for item in data_json:
        if 'college_img' in item:
            # Montar a URL completa para a imagem
            item['image_url'] = url_for('static', filename=f'imgs/{item['college_img']}', _external=True)

    return jsonify(data_json)

