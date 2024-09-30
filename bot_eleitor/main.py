from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.plugins.http import BotHttpPlugin

from webdriver_manager.chrome import ChromeDriverManager

import sys, os 
import requests

module = os.path.abspath(os.path.join(os.path.dirname(__file__), "src"))
sys.path.append(module)

import e_mail, pdf, spreadsheet

BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Primeiro arquivo
file01_link01 = r"C:\voters\matutino\Documents\projects\BotCity\bot_aval_lg\spreadsheet\RelacaoProduto.xlsx"
file01_link02 = r"C:\voters\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_aval_lg\spreadsheet\RelacaoProduto.xlsx"

# Segundo arquivo
file02_link01 = r"C:\voters\matutino\Documents\projects\BotCity\bot_aval_lg\resources\ListaProduto.pdf"
file02_link02 = r"C:\voters\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_aval_lg\resources\ListaProduto.pdf"

# Terceiro arquivo
file03_link01 = r"C:\voters\matutino\Documents\projects\BotCity\bot_aval_lg\resources\SiteProduto.pdf"
file03_link02 = r"C:\voters\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_aval_lg\resources\SiteProduto.pdf"

# Quarto arquivo
file04_link01 = (
    r"C:\voters\matutino\Documents\projects\BotCity\bot_aval_lg\resources\Produtos.pdf"
)
file04_link02 = r"C:\voters\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_aval_lg\resources\Produtos.pdf"

# Anexo do email
attachment_file_path01 = (
    r"C:\voters\matutino\Documents\projects\BotCity\bot_aval_lg\resources\Produtos.pdf"
)
attachment_file_path02 = r"C:\voters\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_aval_lg\resources\Produtos.pdf"

# Funcoes essenciais
def access_site(bot):
    # Acessar o site
    bot.browse("https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral")

    # Clicar na aba 'Titulo Eleitoral'
    while (
        len(bot.find_elements(
            '//*[@id="menu-lateral-res"]/ul/li[8]/a', 
            By.XPATH
        )) < 1
    ):
        bot.wait(1000)
        print("carrengado ...")
    
    bot.wait(1000)

    # Clicar na aba 'Consulta numero do eleitor'
    while (
        len(bot.find_elements(
            '//*[@id="content"]/app-root/div/app-atendimento-eleitor/div[1]/app-menu-option[10]/button/div/span[1]', 
            By.XPATH
        )) < 1
    ):
        bot.wait(1000)
        print("carrengado ...")
    
    bot.wait(1000)

    # Inserir infos no forms

    name = "Carlos Vinicius Monteiro de Souza"
    bot.find_element(
        '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[1]/input', By.XPATH
    ).send_keys(name)

    bot.wait(2000)

    birth_day = "14/01/2001"
    bot.find_element(
        '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[2]/input', By.XPATH
    ).send_keys(birth_day)

    bot.wait(2000)

    mother_name = "14/01/2001"
    bot.find_element(
        '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[3]/div/input', By.XPATH
    ).send_keys(mother_name)

    bot.wait(2000)

    # Infos inseridas

    # Clicar no botao 'Entrar'
    bot.find_element(
        '//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]', By.XPATH
    )


def api_list_voters():
    http = BotHttpPlugin("http://127.0.0.1:5000/voter")

    return http.get_as_json()


def insert_voter(voter):
    url = "http://127.0.0.1:5000/voter"
    headers = {"Content-Type": "application/json"}

    data = {
        'cpf': voter['CPF'],
        'nome': voter['NOME'],
        'data_nascimento': voter['DATA_NASCIMENTO'],
        'nome_mae': voter['NOME_MAE'], 
        'cep': voter['CEP'], 
        'nro_endereco': voter['NRO_ENDERECO'],
        'nro_titulo': voter['NRO_TITULO'], 
        'situacao': voter['SITUACAO'], 
        'secao': voter['SECAO'], 
        'zona': voter['ZONA'], 
        'local_votacao': voter['LOCAL_VOTACAO'], 
        'endereco_votacao': voter['ENDERECO_VOTACAO'], 
        'bairro': voter['BAIRRO'],
        'municipio_uf': voter['MUNICIPIO_UF'], 
        'pais': voter['PAIS']
    }

    try:
        response = requests.post(url=url, headers=headers, json=data)
        response.raise_for_status()
        returnJSON = response.json()

    except requests.exceptions.HTTPError as err:
        print(f"Erro HTTP: {err}")

    except Exception as ex:
        print(f"Erro Exception: {ex}")

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    access_site(bot)
    bot.wait(5000)
    bot.stop_browser()

    # Implement logic

    print("Leitura do arquivo Excel...")
    file_excel = file01_link02
    sheet = "Plan1"

    df = spreadsheet.read_excel(file_excel, sheet)
    spreadsheet.show_data_excel(df)

    print("Inserindo eleitores no banco de data...")
    for index, voter in df.iterrows():
        insert_voter(voter)

    print("Gerando arquivo PDF com a lista de eleitores...")
    votersJSON = api_list_voters()
    list_voter = votersJSON["data"]
    pdf.create_pdf(list_voter)

    print(
        "Gerando arquivo eleitores.pdf com o merge entre os arquivos: ListaEleitor.pdf + SiteEleitor.pdf..."
    )
    list_pdf = []
    list_pdf.append(file02_link02)
    list_pdf.append(file03_link02)
    pdf.merge_pdfs(list_pdf, file04_link02)

    print("Enviando E-mail com a lista de eleitores no arquivo Eleitores.pdf em anexo.")

    attachment_file = attachment_file_path02

    voters_json = api_list_voters()
    list_voters = voters_json["data"]

    for voter in list_voters:
        recipient = voter["email"]
        print(f"Enviando e-mail para: {recipient}")

        topic = "Lista de eleitores"
        content = "<h1>Sistema Automatizado!</h1> Em anexo, a lista de eleitores."
        e_mail.send_email_attachment(recipient, topic, content, attachment_file)

    print("Fim do processamento...")


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == "__main__":
    main()
