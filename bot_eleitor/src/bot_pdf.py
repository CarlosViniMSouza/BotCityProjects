# from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.plugins.http import BotHttpPlugin

# from webdriver_manager.chrome import ChromeDriverManager

from PyPDF2 import PdfMerger

import sys
import os
import requests
import json

import pdf
import spreadsheet

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Primeiro arquivo
file01_link01 = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\RelacaoEleitor.xlsx"

file01_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\RelacaoEleitor.xlsx"

def insert_voter(voter):
    url = "http://127.0.0.1:5000/voter"
    headers = {"Content-Type": "application/json"}

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

def api_get_voters_cep():
    http = BotHttpPlugin("http://127.0.0.1:5000/voter")
    returnJSON = http.get_as_json()

    ceps = [item["cep"] for item in returnJSON["data"]]

    return ceps

def access_api_ceps(cep):
    http = BotHttpPlugin(f"https://viacep.com.br/ws/{id}/json/")

    return http.get_as_json()

def consult_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def bot_merge_pdfs():

    # Mesclar pdfs - Lista de arquivos PDF a serem mesclados
    pdfs = [
        r'C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\ListaCEP.pdf',
        r'C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\1664388206.pdf', 
        r'C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\3525405243.pdf', 
        r'C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\70390243221.pdf'
    ]

    # Cria um objeto PdfMerger
    merger = PdfMerger()

    # Adiciona cada PDF ao objeto merger
    for pdf in pdfs:
        merger.append(pdf)

    # Escreve o PDF mesclado em um novo arquivo
    merger.write(r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\merge_pdfs.pdf")
    merger.close()

def bot_pdf():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    print("Leitura do arquivo Excel...")
    file_excel = file01_link01
    sheet = "CPF"

    df = spreadsheet.read_excel(file_excel, sheet)
    spreadsheet.show_data_excel(df)

    print("Inserindo eleitores no banco de data...")
    for index, item in df.iterrows():
        insert_voter(item)

    print("Acessando API dos CEPs")

    list_ceps = api_get_voters_cep()
    print(list_ceps)

    print("Vendo na API dos CEPs cada endereco")

    ceps_searched = []

    # Consultando cada CEP na lista
    for cep in list_ceps:
        result = consult_cep(cep)

        if result:
            print(f"CEP pesquisado: {cep}")
            print(result)
            print("\n")
            ceps_searched.append(result)

        else:
            print(f"Não foi possível consultar o CEP: {cep}")

    print("Gerando arquivo PDF com a lista de CEPs...")
    pdf.create_pdf_ceps(ceps_searched)
