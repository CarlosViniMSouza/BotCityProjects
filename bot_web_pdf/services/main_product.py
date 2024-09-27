from webdriver_manager.microsoft import EdgeChromiumDriverManager

from datetime import datetime
import requests
import sys, os

from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.plugins.http import BotHttpPlugin

path_pdf = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'pdf'
))
sys.path.append(path_pdf)

path_spreadsheet = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'spreadsheet'
))
sys.path.append(path_spreadsheet)

path_email = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'email'
))
sys.path.append(path_email)

import spreadsheet.spreadsheet as spreadsheet
# import email.email as email
# import pdf.pdf as pdf

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def execute_api():
    http = BotHttpPlugin("https://economia.awesomeapi.com.br/last/USD-BRL")

    return http.get_as_json()

def insert_product(product, dolar_value):
    print(product)

    updated_value = float(dolar_value) * float(product['PRECO_REAL'])

    print(updated_value)

    url = "http://127.0.0.1:5000/product"
    headers = {'Content-Type': 'application/json'}
    data = {
        "description": product['DESCRICAO'],
        "unit": product['UNIDADE'],
        "quantity": product['QUANTIDADE'],
        "real_price": product['PRECO_REAL'],
        "dolar_price": updated_value
    } # I left it in lowercase

    print(data)

    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()
        return_json = response.json()

    except requests.exceptions.HTTPError as err:
        print(f"Error HTTP: {err}")
    
    except Exception as ex:
        print(f"Error Exception: {ex}")

def main():
    print("Part 01")

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.EDGE
    bot.driver_path = EdgeChromiumDriverManager().install()

    # process to execute
    print("Start of processing ...")

    returnJSON = execute_api()
    dolar_value = returnJSON['USDBRL']['high']

    print('Show Spreadsheet')
    df = spreadsheet.read_excel(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_pdf_excel\spreadsheet\RelacaoProduto.xlsx", 'Plan1')

    for index, product in df.iterrows():
        insert_product(product, dolar_value)

    spreadsheet.show_data_excel(df)

    """
    print("Send Email")
    (...)
    """

    bot.wait(5000)
    bot.stop_browser()

    maestro.finish_task(
        task_id=execution.task_id,
        status=AutomationTaskFinishStatus.SUCCESS,
        message="Task Finished OK."
    )

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
