from PyPDF2 import PdfWriter, PdfReader, PdfMerger

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph

from datetime import datetime


def merge_pdfs(list_pdf, file_output):
    merger = PdfMerger()

    for pdf in list_pdf:
        merger.append(pdf)

    merger.write(file_output)
    merger.close()


def create_pdf(products):
    logo01_path = r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\pdf\banner.png"
    logo02_path = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\pdf\banner.png"
    destiny01_path = r"C:\Users\matutino\Documents\projects\BotCity\bot_web_pdf\resources\ListaProduto.pdf"
    destiny02_path = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\bot_web_pdf\resources\ListaProduto.pdf"

    file_logo = logo02_path
    to_file = destiny02_path

    pdf = SimpleDocTemplate(to_file, pagesize=A4)

    styles = getSampleStyleSheet()
    title_style = styles["Title"]
    normal_style = styles["Normal"]
    center_style = ParagraphStyle(
        name="Centerlized", parent=styles["Normal"], alignment=1
    )  # 1 é para centralizar

    image = Image(file_logo, width=320, height=50)
    title = Paragraph("Lista de Produto", title_style)

    date_hour_current = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date_hour_paragraph = Paragraph(f"Data e Hora: {date_hour_current}", center_style)

    # Cria a table_format de data
    data = [["Description", "Unit", "Quantity", "Real Price", "Dolar Price"]]

    for item in products:
        data.append(
            [
                item["description"],
                item["unit"],
                item["quantity"],
                item["real_price"],
                item["dolar_price"],
            ]
        )

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
