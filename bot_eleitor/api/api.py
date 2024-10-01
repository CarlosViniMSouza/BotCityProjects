from flask import Flask, make_response, jsonify, request

import sys
import os

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repository"))
sys.path.append(module)

import voter  # noqa: E402

app_api = Flask("bot_eleitor")
app_api.config["JSON_SORT_KEYS"] = False


# Rota pra inicio da API #
@app_api.route("/", methods=["GET"])
def hello_world():
    return "API do Eleitor - OK"


# -- Inicio: Serviços da api usuário
@app_api.route("/voter", methods=["POST"])
def create_voter():
    voter_json = request.json
    # cpf_voter=0

    try:
        # cpf_voter = voter.create_voter(voter_json)  # noqa: F841
        voter.create_voter(voter_json)
        success = True
        _message = "Eleitor Inserido!"

    except Exception as ex:
        success = False
        _message = f"Erro: {ex}"

    return make_response(jsonify(status=success, message=_message))


@app_api.route("/voter", methods=["GET"])
def list_voters():
    list_voters = list()
    list_voters = voter.list_voters()

    if len(list_voters) == 0:
        success = False
        _message = "Lista vazia"
    else:
        success = True
        _message = "Lista OK"

    return make_response(jsonify(status=success, message=_message, data=list_voters))


@app_api.route("/voter/<int:cpf>", methods=["GET"])
def get_voter_cpf(cpf):
    voter_cpf = list()
    voter_cpf = voter.get_voter_cpf(cpf)

    if len(voter_cpf) == 0:
        success = False
        _message = "Eleitor não encontrado!"
    else:
        success = True
        _message = "Eleitor encontrado!"

    return make_response(jsonify(status=success, _message=_message, data=voter_cpf))


@app_api.route("/voter", methods=["PUT"])
def update_voter():
    voter_json = request.json

    try:
        voter.update_voter(voter_json)
        success = True
        _message = "Infos eleitor atualizadas"

    except Exception as ex:
        success = False
        _message = f"Erro: {ex}"

    return make_response(jsonify(status=success, message=_message))


@app_api.route("/voter/<int:cpf>", methods=["DELETE"])
def delete_voter(cpf):
    try:
        voter.delete_voter(cpf)
        success = True
        _message = "Eleitor removido!"

    except Exception as ex:
        success = False
        _message = f"Erro: {ex}"

    return make_response(jsonify(status=success, mensagem=_message))


app_api.run()
