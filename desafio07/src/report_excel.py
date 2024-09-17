from botcity.plugins.excel import BotExcelPlugin

def report_excel():
    # Instancie o plugin
    bot_excel = BotExcelPlugin()

    # Leia em um arquivo do Excel
    bot_excel.read('read.xlsx')
    # Adicione uma linha
    bot_excel.add_row([0, 22])
    # Classifique pelas colunas A e B em ordem descendente
    bot_excel.sort(['a', 'b'], False)

    # Imprima o resultado
    print(bot_excel.as_list())
    # Salve -o em um novo arquivo
    bot_excel.write('write.xlsx')

report_excel()
