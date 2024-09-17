import pandas as pd
import numpy as np

import plotly.express as px
import plotly.figure_factory as ff

import matplotlib.pyplot as plt
import seaborn as sns

def data_analysis():
    CSV_URL = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
    PATH_CSV = r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\csv\dataset.csv"

    dataset = pd.read_csv(PATH_CSV, sep=",")
    sample = dataset.sample(frac=0.1, replace=True, random_state=1)

    # """
    # dataset.to_csv(
    #     r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\csv\dataset.csv"
    # )  # salvar o CSV da web
    #
    # sample.to_csv(
    #     r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\csv\sample.csv"
    # )  # salvar a amostra
    # """

    # substituir valores nulos
    dataset.replace(np.nan, 0, inplace=True)
    sample.replace(np.nan, 0, inplace=True)

    dataset_info = dataset.info()
    print(dataset_info)

    dataset_describe = dataset.describe()
    print(dataset_describe)

    # selecionando amostras vindas do Brasil, Argentina e Chile
    sample_brazil = sample[sample['country'] == 'Brazil']
    sample_argen = sample[sample['country'] == 'Argentina']
    sample_chile = sample[sample['country'] == 'Chile']

    # unindo as 3 amostras em 1
    frames = [sample_brazil, sample_argen, sample_chile]
    sampleMerged= pd.concat(frames)

    # Plotando os dados no tempo
    fig = px.histogram(
        sample_brazil,
        title='Quantidade de Novos Casos de Covid-19 (Brasil)',
        labels={'date': 'Meses de 2020 a 2023', 'new_cases': 'Novos Casos'},
        x="date",
        y="new_cases"
    )

    fig.update_layout(bargap=0.1)
    fig.show()
    plt.savefig(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img01.png")

    # Plotando os dados no tempo
    fig = px.histogram(
        sample_argen,
        title='Quantidade de Novos Casos de Covid-19 (Argentina)',
        labels={'date': 'Meses de 2020 a 2023', 'new_cases': 'Novos Casos'},
        x="date",
        y="new_cases"
    )

    fig.update_layout(bargap=0.1)
    fig.show()
    plt.savefig(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img02.png")

    # Plotando os dados no tempo
    fig = px.histogram(
        sample_chile,
        title='Quantidade de Novos Casos de Covid-19 (Chile)',
        labels={'date': 'Meses de 2020 a 2023', 'new_cases': 'Novos Casos'},
        x="date",
        y="new_cases"
    )

    fig.update_layout(bargap=0.1)
    fig.show()
    plt.savefig(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img03.png")

    # Vendo a correlação das colunas númericas da amostra do Brasil
    sample_brazil_corr = sample_brazil.drop(columns=['code', 'continent', 'country', 'date'])

    sns.heatmap(sample_brazil_corr.corr())
    plt.savefig(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img05.png")

    # Comparando os Novos Casos das amostras de Brasil, Argentina e Chile
    sns.set_theme(style="darkgrid")
    sns.lineplot(
        x="date",
        y="new_cases",
        hue="country",
        data=sampleMerged
    )
    plt.show()
    plt.savefig(r"C:\Users\CarlosViniMSouza\Documents\Projects\BotCityProjects\desafio07\assets\images\img04.png")

data_analysis()
