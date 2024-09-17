from botcity.core import DesktopBot

def report_calc():
    path = r"C:\Program Files\LibreOffice\program\scalc.exe"

    bot = DesktopBot()    
    bot.execute(path)

# report_calc()
