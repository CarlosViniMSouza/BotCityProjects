from flask import Flask, make_response, jsonify, request, Response

import sys, os

module = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'repository'
))
sys.path.append(module)

import product

app_api = Flask('api_database')
app_api.config['JSON_SORT_KEYS'] = False

# Rota pra inicio da API #
@app_api.route('/', methods=['GET'])
def hello_world():
    return "Hello, Fantastic World"

# -- Inicio : Serviços da api product ---------------------

@app_api.route('/product', methods=['POST'])
def create_product():
    product_json = request.json
    id_product=0

    try:
        id_product = product.create_product(product_json)
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

app_api.run()

# -- Fim : Serviços da api product ---------------------