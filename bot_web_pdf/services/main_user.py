from webdriver_manager.chrome import ChromeDriverManager

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

def insert_user(user):
    print(user + "\n")

    url = "http://127.0.0.1:5000/user"
    headers = {'Content-Type': 'application/json'}
    data = {
        "name": user['NOME'],
        "login": user['LOGIN'],
        "email": user['EMAIL'],
        "password": user['SENHA'],
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
    print("Part 01\n")

    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    # process to execute
    print("Start of processing ...")

    print('Show Spreadsheet')
    df = spreadsheet.read_excel(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_pdf_excel\spreadsheet\RelacaoUsuario.xlsx", 'Plan1')

    for index, user in df.iterrows():
        insert_user(user)

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
