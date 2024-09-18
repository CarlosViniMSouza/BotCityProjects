from flask import Flask, make_response, jsonify, request, Response

import sys, os

module = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'repository'))
sys.path.append(module)

import user 
import product

app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Implementar a lógica de programação

# -- Inicio: Serviços da api usuário ---------------------

@app_api.route('/user', methods=['GET'])
def get_list_users():
    list_user = list()
    list_user = user.list_users()
    if len(list_user) == 0:
        success = False
        _message = 'List Empty'
    else:
        success = True
        _message = 'List User OK'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = success, 
                message = _message,
                data = list_user
        )
    )

@app_api.route('/user/<int:id>', methods=['GET'])
def get_user_id(id):
    user_id = list()
    user_id = user.get_user_id(id)
    if len(user_id) == 0:
        success = False
        _message = 'user not found'
    else:
        success = True
        _message = 'user founded'

    # Construir um Response
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = success, 
                _message = _message,
                data = user_id
        )
    )

@app_api.route('/user', methods=['POST'])
def create_user():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    user_json = request.json # corpo da requisição
    try:
        id_user = user.create_user(user_json)
        success = True
        _message = 'User inserted sucessfully'
    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = success,
                message = _message ,
                id = id_user
        )
    )

@app_api.route('/user', methods=['PUT'])
def update_user():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    user_json = request.json # corpo da requisição
    try:
        user.update_user(user_json)
        success = True
        _message = 'User updated successfully'
    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = success,
                message = _message
        )
    )

@app_api.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user.delete_user(id)
        success = True
        _message = 'User deleted successfully'
    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = success,
                mensagem = _message
        )
    )    

# -- Fim: Serviços da api usuário ---------------------

# -- Inicio : Serviços da api product ---------------------
@app_api.route('/product', methods=['POST'])
def create_product():
    # Construir um Request
    # Captura o JSON com os dados enviado pelo cliente
    product_json = request.json # corpo da requisição
    id_product=0
    try:
        id_product = product.create_product(product_json)
        success = True
        _message = 'product insert successfully'
    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        # Formata a resposta no formato JSON
        jsonify(
                status = success,
                message = _message ,
                id = id_product
        )
    )

# Execute
app_api.run()