from PyPDF2 import PdfWriter, PdfFileReader, PageObject

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def millimeters_points():
    pdf_writer = PdfWriter()

    new_page = PageObject.create_blank_page(width=595.2, height=841.8)
    pdf_writer.add_page(new_page)

    with open("meu_arquivo.pdf", "wb") as output_pdf:
        pdf_writer.write(output_pdf)

"""
width = largura
height = altura
"""

def create_pdf():
    width, height = A4

    pdf = canvas.Canvas('./teste.pdf', pagesize=A4)
    pdf.setFont('Helvetica', 16)

    title = 'AvaliacaoParte01'
    print(len(title))

    pdf.drawString(((width / 2) - (len(title) / 2)), height - 90, title)
    pdf.save()
