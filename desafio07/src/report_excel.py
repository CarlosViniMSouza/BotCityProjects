import openpyxl
import os

if not os.path.exists(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\docs"):
    os.mkdir(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\docs")

def report_excel():
    wrkb = openpyxl.Workbook()
  
    # Numero de planilhas
    ws = wrkb.worksheets[0]
    
    # Inserir imagem01
    img1 = openpyxl.drawing.image.Image(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img01.png") 
    img1.anchor = 'A2'
    ws.add_image(img1)

    img2 = openpyxl.drawing.image.Image(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img02.png") 
    img2.anchor = 'M2'
    ws.add_image(img2)

    img3 = openpyxl.drawing.image.Image(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img03.png") 
    img3.anchor = 'A28'
    ws.add_image(img3)

    img4 = openpyxl.drawing.image.Image(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img04.png") 
    img4.anchor = 'M28'
    ws.add_image(img4)

    # Salvar em um novo .xlsx
    wrkb.save(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\docs\report.xlsx")

# report_excel() -> descomente para executar isoladamente
