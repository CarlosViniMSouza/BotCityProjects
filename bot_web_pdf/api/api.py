from flask import Flask, make_response, jsonify, request, Response

import sys, os

module = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'repository'
))
sys.path.append(module)

import product, user

app_api = Flask('bot_pdf_excel')
app_api.config['JSON_SORT_KEYS'] = False

# Rota pra inicio da API #
@app_api.route('/', methods=['GET'])
def hello_world():
    return "Hello, Fantastic World"

# -- Inicio: Serviços da api usuário
@app_api.route('/user', methods=['POST'])
def create_user():
    user_json = request.json
    id_user=0

    try:
        id_user = user.create_user(user_json)
        success = True
        _message = 'User inserted sucessfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            message = _message,
            id = id_user
        )
    )

@app_api.route('/users', methods=['GET'])
def list_users():
    list_users = list()
    list_users = user.list_users()

    if len(list_users) == 0:
        success = False
        _message = 'List Empty'
    else:
        success = True
        _message = 'List User OK'

    return make_response(
        jsonify(
            status = success, 
            message = _message,
            data = list_users
        )
    )

@app_api.route('/user/<int:id>', methods=['GET'])
def get_user_id(id):
    user_id = list()
    user_id = user.get_user_id(id)

    if len(user_id) == 0:
        success = False
        _message = 'User not found'
    else:
        success = True
        _message = 'User founded'

    return make_response(
        jsonify(
            status = success, 
            _message = _message,
            data = user_id
        )
    )

@app_api.route('/user', methods=['PUT'])
def update_user():
    user_json = request.json

    try:
        user.update_user(user_json)
        success = True
        _message = 'User updated successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
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
        jsonify(
            status = success,
            mensagem = _message
        )
    ) 

# -- Inicio: Serviços da api product
@app_api.route('/product', methods=['POST'])
def create_product():
    product_json = request.json
    id_product=0

    try:
        id_product = product.create_product(product_json)
        product.update_dolar_price(product_json)

        success = True
        _message = 'product insert successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            message = _message,
            id = id_product
        )
    )

@app_api.route('/products', methods=['GET'])
def list_products():
    list_products = list()
    list_products = product.list_products()

    if len(list_products) == 0:
        success = False
        _message = 'List Empty'
    else:
        success = True
        _message = 'List product: OK'

    return make_response(
        jsonify(
            status = success, 
            message = _message,
            data = list_products
        )
    )

@app_api.route('/product/<int:id>', methods=['GET'])
def get_product_id(id):
    product_id = list()
    product_id = product.get_product_id(id)

    if len(product_id) == 0:
        success = False
        _message = 'Product not found'
    else:
        success = True
        _message = 'Product founded'

    return make_response(
        jsonify(
            status = success, 
            _message = _message,
            data = product_id
        )
    )

@app_api.route('/product', methods=['PUT'])
def update_product():
    product_json = request.json

    try:
        product.update_product(product_json)
        success = True
        _message = 'Product updated successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            message = _message
        )
    )

@app_api.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    try:
        product.delete_product(id)
        success = True
        _message = 'Product deleted successfully'

    except Exception as ex:
        success = False
        _message = f'Erro: {ex}'
    
    return make_response(
        jsonify(
            status = success,
            mensagem = _message
        )
    ) 

app_api.run()