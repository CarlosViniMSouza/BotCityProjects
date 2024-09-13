from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot, Browser, By
from botcity.maestro import *

# data science
import pandas as pd
import matplotlib.pyplot as plt

# others
import csv
import requests

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    # bot = WebBot()
    # bot.headless = False
    # bot.browser = Browser.CHROME
    # bot.driver_path = ChromeDriverManager().install()

    # push and sabe .csv file
    CSV_URL = 'https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv'

    dataset = pd.read_csv(CSV_URL)

    print(dataset.head(10))
    print(dataset.info())

    dataset.to_csv(r'C:\Users\matutino\Documents\projects\BotCity\desafio05\utils\dataset.csv') # save .csv

    # data processing and visualization
    fig, ax = plt.subplots(r'C:\Users\matutino\Documents\projects\BotCity\desafio05\utils\sample.csv')

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    plt.show()

    # stop!
    # bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
