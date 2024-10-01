from flask import jsonify, Blueprint, url_for
import pandas as pd
import os

course_api_blueprint = Blueprint('course_api', __name__, static_folder='static-course_api')

@course_api_blueprint.route('/courses')
def get_course():

    csv_path = os.path.join(course_api_blueprint.root_path, 'static-course_api/CSV_DB/Course_DB.csv')
    db = pd.read_csv(csv_path, delimiter=';')

    data_json = db.to_dict(orient='records')
    
    return jsonify(data_json)

@course_api_blueprint.route('/course-images')
def get_course_images():
    # Caminho para o arquivo CSV
    csv_path = os.path.join(course_api_blueprint.root_path, 'static-course_api/CSV_DB/Course_Image_DB.csv')
    # Ler o CSV usando pandas
    db = pd.read_csv(csv_path, delimiter=';')

    # Converter DataFrame para lista de dicionários
    data_json = db.to_dict(orient='records')

    # Adicionar URL base para as imagens
    for item in data_json:
        if 'img_name' in item:
            # Montar a URL completa para a imagem
            item['course_image_url'] = url_for('course_api.static', filename=f'imgs/{item['img_name']}', _external=True)

    return jsonify(data_json)
