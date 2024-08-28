from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

image_folder = os.path.join(app.root_path, 'static/imgs')

@app.route('/')
def get_faculty():
    # Carrega os dados do Excel
    db = pd.read_csv('Faculdade-DB.csv', delimiter=';')

    # Cria a coluna de URLs das imagens
    db['image_url'] = db['img_faculdade'].apply(lambda x: f'https://c3e1bccd-e40f-4642-a5e0-6b45d108af4b-00-3g9s82kxsdncm.picard.replit.dev/static/imgs/{x}')

    # Converte o DataFrame para uma lista de dicionários
    data_json = db.to_dict(orient='records')

    # Retorna os dados como JSON
    return jsonify(data_json)

@app.route('/static/imgs/<path:filename>')
def get_image(filename):
    # Envia a imagem da pasta estática
    return send_from_directory(image_folder, filename)

@app.route('/courses')
def get_course():
    db = pd.read_csv('Curso-DB.csv', delimiter=';')
    data_json = db.to_dict(orient='records')

    # Retorna os dados como JSON
    return jsonify(data_json)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
