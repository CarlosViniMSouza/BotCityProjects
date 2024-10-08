from botcity.web import WebBot, Browser, By
from botcity.maestro import *  # noqa: F403
from botcity.plugins.http import BotHttpPlugin  # type: ignore

from webdriver_manager.chrome import ChromeDriverManager

import sys, os  # noqa: E401
import requests

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(module)

import e_mail, pdf, spreadsheet  # type: ignore # noqa: E401, E402

# import email.email as email
# import pdf.pdf as pdf
# import spreadsheet.spreadsheet as spreadsheet

file01_link01 = r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\spreadsheet\RelacaoProduto.xlsx"
file01_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\spreadsheet\RelacaoProduto.xlsx"

file02_link01 = r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\resources\ListaProduto.pdf"
file02_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\resources\ListaProduto.pdf"

file03_link01 = r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\resources\SiteProduto.pdf"
file03_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\resources\SiteProduto.pdf"

file04_link01 = (
    r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\resources\Produtos.pdf"
)
file04_link02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\resources\Produtos.pdf"

attachment_file_path01 = (
    r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\resources\Produtos.pdf"
)
attachment_file_path02 = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\resources\Produtos.pdf"


def access_site(bot):
    # Acessar site
    bot.browse("https://flordejambu.com/shop/")

    while (
        len(
            bot.find_elements(
                "/html/body/div[1]/header/div/div[1]/div/div/div[1]/div/a/img", By.XPATH
            )
        )
        < 1
    ):
        bot.wait(1000)
        print("carrengado.")
    bot.wait(1000)

    # Perquisar pelo product
    product = "Açai"
    bot.find_element(
        "/html/body/div[1]/header/div/div[1]/div/div/div[2]/div/form/input[1]", By.XPATH
    ).send_keys(product)
    bot.wait(1000)
    bot.enter()
    bot.wait(1000)
    # Imprimir página do site para arquivo PDF
    bot.print_pdf(file03_link02)


def api_get_dolar_value():
    http = BotHttpPlugin("https://economia.awesomeapi.com.br/last/USD-BRL")

    return http.get_as_json()


def api_list_products():
    http = BotHttpPlugin("http://127.0.0.1:5000/product")

    return http.get_as_json()


def api_list_users():
    http = BotHttpPlugin("http://127.0.0.1:5000/user")

    return http.get_as_json()


def insert_product(product, dolar_value):
    url = "http://127.0.0.1:5000/product"
    headers = {"Content-Type": "application/json"}
    updated_value = float(dolar_value) * float(product["PRECO_REAL"])

    data = {
        "description": product["DESCRICAO"],
        "unit": product["UNIDADE"],
        "quantity": product["QUANTIDADE"],
        "real_price": product["PRECO_REAL"],
        "dolar_price": updated_value,
    }

    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()
        # returnJSON = response.json()

    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")

    except Exception as ex:
        print(f"Erro Exception: {ex}")


BotMaestroSDK.RAISE_NOT_CONNECTED = False  # noqa: F405


def main():
    maestro = BotMaestroSDK.from_sys_args()  # noqa: F405
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    access_site(bot)
    bot.wait(3000)
    bot.stop_browser()

    # Implement logic

    print("Inicio do processamento...")
    print("Acesso API Cotacao Dolar...")

    returnJSON = api_get_dolar_value()
    dolar_value = returnJSON["USDBRL"]["high"]

    print("Leitura do arquivo Excel...")
    file_excel = file01_link02
    sheet = "Plan1"

    df = spreadsheet.read_excel(file_excel, sheet)
    spreadsheet.show_data_excel(df)

    print("Inserindo produtos no banco de data...")
    for index, product in df.iterrows():
        insert_product(product, dolar_value)

    print("Gerando arquivo PDF com a lista de produtos...")
    returnJSONProducts = api_list_products()
    list_product = returnJSONProducts["data"]
    pdf.create_pdf(list_product)

    print(
        "Gerando arquivo produtos.pdf com o merge entre os arquivos: ListaProduto.pdf + SiteProduto.pdf..."
    )
    list_pdf = []
    list_pdf.append(file02_link02)
    list_pdf.append(file03_link02)
    pdf.merge_pdfs(list_pdf, file04_link02)

    print("Enviando E-mail para a lista de usuario com arquivo Produtos.pdf em anexo.")

    attachment_file = attachment_file_path02

    users_json = api_list_users()
    list_users = users_json["data"]

    for user in list_users:
        recipient = user["email"]
        print(f"Enviando e-mail para: {recipient}")

        topic = "Lista de produtos"
        content = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de products."
        e_mail.send_email_attachment(recipient, topic, content, attachment_file)

    print("Fim do processamento...")


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
