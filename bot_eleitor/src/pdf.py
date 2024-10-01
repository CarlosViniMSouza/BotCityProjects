from PyPDF2 import PdfMerger  # type: ignore

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph

from datetime import datetime


def merge_pdfs(list_pdf, file_output):
    merger = PdfMerger()

    for pdf in list_pdf:
        merger.append(pdf)

    merger.write(file_output)
    merger.close()


def create_pdf_voters(voters):
    # logo01_path = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\banner.png"
    logo02_path = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\banner.png"

    # destiny01_path = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\ListaCEP.pdf"
    destiny02_path = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\ListaEleitores.pdf"

    file_logo = logo02_path
    to_file = destiny02_path

    pdf = SimpleDocTemplate(to_file, pagesize=A4)

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["Normal"]  # noqa: F841
    center_style = ParagraphStyle(
        name="Centerlized", parent=styles["Normal"], alignment=1
    )  # 1 é para centralizar

    image = Image(file_logo, width=320, height=50)
    title = Paragraph("Lista de Eleitores", title_style)

    date_hour_current = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_hour_paragraph = Paragraph(f"Data e Hora: {date_hour_current}", center_style)

    # Cria a table_format de data
    data = [[
        "cep",
        "nome",
        "data_nascimento",
        "nome_mae",
        "cep",
        "nro_endereco",
    ]]

    for info in voters:
        data.append([
            info["CPF"],
            info["NOME"],
            info["DATA_NASCIMENTO"],
            info["NOME_MAE"],
            info["CEP"],
            info["NRO_ENDERECO"],
        ])

    # Cria a table_format
    table_format = Table(data)

    # Define o estilo da table_format
    table_style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )

    table_format.setStyle(table_style)

    # Adiciona os elementos ao documento
    elements = [image, title, date_hour_paragraph, table_format]
    pdf.build(elements)

def create_pdf_ceps(ceps):
    # logo01_path = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\banner.png"
    logo02_path = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\banner.png"

    # destiny01_path = r"C:\Users\matutino\Documents\projects\BotCity\bot_eleitor\resources\ListaCEP.pdf"
    destiny02_path = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_eleitor\resources\ListaCEPs.pdf"

    file_logo = logo02_path
    to_file = destiny02_path

    pdf = SimpleDocTemplate(to_file, pagesize=A4)

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["Normal"]  # noqa: F841
    center_style = ParagraphStyle(
        name="Centerlized", parent=styles["Normal"], alignment=1
    )  # 1 é para centralizar

    image = Image(file_logo, width=280, height=80)
    title = Paragraph("Lista de CEPs", title_style)

    date_hour_current = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_hour_paragraph = Paragraph(f"Data e Hora: {date_hour_current}", center_style)

    # Cria a table_format de data
    data = [[
        "Cep",
        "Logradouro",
        "Complemento",
        "Unidade",
        "Bairro",
        "Localidade",
        "Uf",
        "Estado",
        "Regiao",
        "Ibge",
        "Gia",
        "Ddd",
        "Siafi"
    ]]

    for info in ceps:
        data.append([
            info["cep"],
            info["logradouro"],
            info["complemento"],
            info["unidade"],
            info["bairro"],
            info["localidade"],
            info["uf"],
            info["estado"],
            info["regiao"],
            info["ibge"],
            info["gia"],
            info["ddd"],
            info["siafi"]
        ])

    # Cria a table_format
    table_format = Table(data)

    # Define o estilo da table_format
    table_style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )

    table_format.setStyle(table_style)

    # Adiciona os elementos ao documento
    elements = [image, title, date_hour_paragraph, table_format]
    pdf.build(elements)