# from botcity.web import WebBot, Browser, By
from botcity.maestro import *  # noqa: F403
# from botcity.plugins.http import BotHttpPlugin

# from webdriver_manager.chrome import ChromeDriverManager

import sys
import os
import requests
import json

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(module)

# import e_mail
# import pdf
import spreadsheet  # noqa: E402

BotMaestroSDK.RAISE_NOT_CONNECTED = False  # noqa: F405

# Primeiro arquivo
file01_link01 = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\RelacaoEleitor.xlsx"
file01_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\RelacaoEleitor.xlsx"


def insert_voter(voter):
    url = "http://127.0.0.1:5000/voter"
    headers = {"Content-Type": "application/json"}

    # data = {
    #     'cpf': voter['CPF'],
    #     'nome': voter['NOME'],
    #     'data_nascimento': voter['DATA_NASCIMENTO'],
    #     'nome_mae': voter['NOME_MAE'],
    #     'cep': voter['CEP'],
    #     'nro_endereco': voter['NRO_ENDERECO'],
    #     'nro_titulo': voter['NRO_TITULO'],
    #     'situacao': voter['SITUACAO'],
    #     'secao': voter['SECAO'],
    #     'zona': voter['ZONA'],
    #     'local_votacao': voter['LOCAL_VOTACAO'],
    #     'endereco_votacao': voter['ENDERECO_VOTACAO'],
    #     'bairro': voter['BAIRRO'],
    #     'municipio_uf': voter['MUNICIPIO_UF'],
    #     'pais': voter['PAIS']
    # }

    data = {
        "cpf": voter["CPF"],
        "nome": voter["NOME"],
        "data_nascimento": json.dumps(str(voter["DATA_NASCIMENTO"])),
        "nome_mae": voter["NOME_MAE"],
        "cep": voter["CEP"],
        "nro_endereco": voter["NRO_ENDERECO"],
    }

    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()
        returnJSON = response.json()

        return returnJSON

    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")

    except Exception as ex:
        print(f"Erro Exception: {ex}")


def main():
    maestro = BotMaestroSDK.from_sys_args()  # noqa: F405
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    print("Leitura do arquivo Excel...")
    file_excel = file01_link02
    sheet = "CPF"

    df = spreadsheet.read_excel(file_excel, sheet)
    spreadsheet.show_data_excel(df)

    print("Inserindo eleitores no banco de data...")
    for index, item in df.iterrows():
        insert_voter(item)


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
