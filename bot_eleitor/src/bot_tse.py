
from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from botcity.plugins.http import BotHttpPlugin

# from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from PyPDF2 import PdfReader, PdfWriter

from pdf import merge_pdfs
from spreadsheet import read_excel

import requests


def extract_data(bot):
    data = {}

    data['nro_titulo'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/div[1]/p[1]/b', By.XPATH).text
    data['situacao'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/div[1]/p[2]/span', By.XPATH).text
    data['secao'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[1]/span[2]', By.XPATH).text
    data['zona'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[2]/div[3]/span[2]', By.XPATH).text
    data['local_votacao'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[1]/span[2]', By.XPATH).text
    data['endereco_votacao'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[2]/span[2]', By.XPATH).text
    data['bairro'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[4]/span[2]', By.XPATH).text
    data['municipio_uf'] = bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[1]/app-box-local-votacao/div/div/div[1]/div[3]/span[2]', By.XPATH).text
    data['pais'] = "Brasil"  # Supondo que o país seja fixo

    return data


def print_data_extracted(voter, mother, birthday, cpf, data_extracted):
    # Formata a data de nascimento para dd/mm/aa
    birthday_format = birthday[:2] + '/' + birthday[2:4] + '/' + birthday[4:]  # (dd/mm/aa)
    
    print("\n=== data Extraídos ===")
    print(f"Nome: {voter}")
    print(f"Mãe: {mother}")
    print(f"Data de Nascimento: {birthday_format}")
    print(f"CPF: {cpf}")
    print(f"Número do Título: {data_extracted['nro_titulo']}")
    print(f"Situação: {data_extracted['situacao']}")
    print(f"Seção: {data_extracted['secao']}")
    print(f"Zona: {data_extracted['zona']}")
    print(f"Local de Votação: {data_extracted['local_votacao']}")
    print(f"Endereço de Votação: {data_extracted['endereco_votacao']}")
    print(f"Bairro: {data_extracted['bairro']}")
    print(f"Município/UF: {data_extracted['municipio_uf']}")
    print(f"País: {data_extracted['pais']}")
    print("========================\n")


def access_tse_site(bot, file_excel):
    bot.browse("https://www.tse.jus.br/servicos-eleitorais/titulo-eleitoral")

    # Espera o site carregar
    while len(bot.find_elements('//*[@id="visual-portal-wrapper"]/nav/div/div/h1/a/img', By.XPATH)) < 1:
        bot.wait(1000)
        print('carregando.')
    bot.wait(1000)
    
    # Fechar o modal de cookies
    bot.find_element('//*[@id="modal-lgpd"]/div/div/div[2]/button', By.XPATH).click()
    
    # Lê os data da planilha
    df = read_excel(file_excel, 'CPF')  # Supondo que essa função retorne um DataFrame

    bot.find_element('//*[@id="menu-lateral-res"]/ul/li[8]/a', By.XPATH).click()
    bot.wait(1000)

    list_pdf = []  # Define a lista aqui

    for index, row in df.iterrows():
        voter = row['NOME']
        mother = row['NOME_MAE']
        birthday = row['DATA_NASCIMENTO'].strftime('%d%m%Y')  # Formata a data
        cpf = row['CPF']
        
        # Acessa a seção de atendimento ao eleitor
        bot.find_element('//*[@id="content"]/app-root/div/app-atendimento-eleitor/div[1]/app-menu-option[10]/button/div/span[2]', By.XPATH).click()
        bot.wait(3000)

        # Preenche os data do eleitor
        bot.find_element('//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[1]/input', By.XPATH).send_keys(voter)
        bot.wait(3000)
        bot.find_element('//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[3]/div/input', By.XPATH).send_keys(mother)
        bot.wait(3000)
        bot.find_element('//*[@id="modal"]/div/div/div[2]/div[2]/form/div[1]/div[2]/input', By.XPATH).send_keys(birthday)
        bot.wait(3000)
        bot.find_element('//*[@id="modal"]/div/div/div[2]/div[2]/form/div[2]/button[2]', By.XPATH).click()
        bot.wait(3000)

        # função - Extrai data da página
        data_extracted = extract_data(bot)

        # função - Chama a função para imprimir os data extraídos
        print_data_extracted(voter, mother, birthday, cpf, data_extracted)

        # Salva o PDF com o nome completo
        file_pdf = f'{cpf}_{data_extracted["nro_titulo"]}.pdf'  # Adicione a extensão .pdf aqui
        path_pdf = fr'C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\{file_pdf}'
        bot.print_pdf(path_pdf)

        # Aguardar um pouco para garantir que o PDF foi salvo
        bot.wait(2000)

        # Adiciona o caminho completo do PDF à lista
        list_pdf.append(path_pdf)

        # Voltar à tela anterior
        bot.find_element('//*[@id="content"]/app-root/div/app-consultar-numero-titulo-eleitor/div[2]/button', By.XPATH).click()  # Botão de voltar
        bot.wait(1000)
        bot.refresh()
        bot.wait(1000)

    # Chama a função de mesclagem após processar todos os eleitores
    if list_pdf:
        path_output = r'C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\ArquivosMesclados.pdf'
        merge_pdfs(list_pdf, path_output)
        print(f"PDFs mesclados em: {path_output}")

    print('Todos os eleitores foram processados.')


def bot_tse():
    bot = WebBot()
    bot.headless = False

    # bot.browser = Browser.CHROME
    # bot.driver_path = ChromeDriverManager().install()

    bot.browser = Browser.EDGE
    bot.driver_path = EdgeChromiumDriverManager().install()
    
    print('Inicio do processamento...')
    bot.start_browser()
    bot.maximize_window()
    file_excel = r'C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\RelacaoEleitor.xlsx'
    access_tse_site(bot, file_excel)

    print('Fim do processamento...')
    bot.stop_browser()
