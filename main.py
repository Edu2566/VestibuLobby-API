from flask import Flask, jsonify, send_from_directory
import pandas as pd
import os

app = Flask(__name__)

image_folder = os.path.join(app.root_path, 'static/imgs')

@app.route('/')
def get_faculty():
    # Carrega os dados do Excel
    db = pd.read_excel('Faculdade-DB.xlsx')

    # Cria a coluna de URLs das imagens
    db['image_url'] = db['img_faculdade'].apply(lambda x: f'https://f839e9a8-9bc7-43c5-83ac-49861251fa78-00-gfzzlif47had.worf.replit.dev/static/imgs/{x}')

    # Converte o DataFrame para uma lista de dicionários
    data_json = db.to_dict(orient='records')

    # Retorna os dados como JSON
    return jsonify(data_json)

@app.route('/static/imgs/<path:filename>')
def get_image(filename):
    # Envia a imagem da pasta estática
    return send_from_directory(image_folder, filename)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
