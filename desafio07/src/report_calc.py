from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def report_calc():
    bot = DesktopBot()
    
    path=r"C:\Program Files\LibreOffice\program\scalc.exe"
    
    bot.execute(path)

report_calc()
