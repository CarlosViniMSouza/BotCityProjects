# from botcity.web import WebBot, Browser, By
from botcity.maestro import *
# from botcity.plugins.http import BotHttpPlugin

# from webdriver_manager.chrome import ChromeDriverManager

import sys, os 
import requests

import pandas, json

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(module)

import e_mail, pdf, spreadsheet

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Primeiro arquivo
file01_link01 = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\RelacaoEleitor.xlsx"
file01_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\RelacaoEleitor.xlsx"

def insert_voter(voter):
    url = "http://127.0.0.1:5000/voter"
    headers = {"Content-Type": "application/json"}

    # data = {
    #     'cpf': voter['CPF'],
    #     'nome': voter['NOME'],
    #     'data_nascimento': json.dumps(str(voter['DATA_NASCIMENTO'])),
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
        'cpf': voter['CPF'],
        'nome': voter['NOME'],
        'data_nascimento': json.dumps(str(voter['DATA_NASCIMENTO'])),
        'nome_mae': voter['NOME_MAE'], 
        'cep': voter['CEP'],
        'nro_endereco': voter['NRO_ENDERECO'],
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
    print("Part 01\n")

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # bot = WebBot()
    # bot.headless = False
    # bot.browser = Browser.CHROME
    # bot.driver_path = ChromeDriverManager().install()

    # process to execute
    print("Processando ...\n")

    print("Leitura do arquivo Excel...\n")
    file_excel = file01_link01
    sheet = "CPF"

    df = spreadsheet.read_excel(file_excel, sheet)

    for index, user in df.iterrows():
        insert_voter(user)

    spreadsheet.show_data_excel(df)

    # bot.wait(5000)
    # bot.stop_browser()

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
