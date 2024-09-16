import pandas as pd
import numpy as np

import plotly.express as px
import plotly.figure_factory as ff

import matplotlib.pyplot as plt
import seaborn as sns

def data_analysis():
    CSV_URL = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"

    dataset = pd.read_csv(CSV_URL, sep=",")
    sample = dataset.sample(frac=0.1, replace=True, random_state=1)

    dataset.to_csv(
        r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\csv\dataset.csv"
    )  # salvar o CSV da web


    sample.to_csv(
        r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\csv\sample.csv"
    )  # salvar a amostra

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
    print(sampleMerged.head(5))

    # buscando infos estatisticas do Brasil
    infos_total_cases = [
    sample_brazil['total_cases'].mean(),
    sample_brazil['total_cases'].mode().iat[0],
    sample_brazil['total_cases'].median(),
    sample_brazil['total_cases'].max() - sample_brazil['total_cases'].min(),
    sample_brazil['total_cases'].var(),
    sample_brazil['total_cases'].std()
    ]

    infos_new_cases = [
    sample_brazil['new_cases'].mean(),
    sample_brazil['new_cases'].mode().iat[0],
    sample_brazil['new_cases'].median(),
    sample_brazil['new_cases'].max() - sample_brazil['new_cases'].min(),
    sample_brazil['new_cases'].var(),
    sample_brazil['new_cases'].std()
    ]

    sample_brazil['new_cases_smoothed_per_million'] = pd.to_numeric(sample_brazil['new_cases_smoothed_per_million'], errors='coerce')

    infos_new_cases_smoothed = [
    sample_brazil['new_cases_smoothed_per_million'].mean(),
    sample_brazil['new_cases_smoothed_per_million'].mode().iat[0],
    sample_brazil['new_cases_smoothed_per_million'].median(),
    sample_brazil['new_cases_smoothed_per_million'].max() - sample_brazil['new_cases_smoothed_per_million'].min(),
    sample_brazil['new_cases_smoothed_per_million'].var(),
    sample_brazil['new_cases_smoothed_per_million'].std()
    ]

    infos_new_deaths = [
    sample_brazil['new_deaths'].mean(),
    sample_brazil['new_deaths'].mode().iat[0],
    sample_brazil['new_deaths'].median(),
    sample_brazil['new_deaths'].max() - sample_brazil['new_deaths'].min(),
    sample_brazil['new_deaths'].var(),
    sample_brazil['new_deaths'].std()
    ]

    infos_total_deaths = [
    sample_brazil['total_deaths'].mean(),
    sample_brazil['total_deaths'].mode().iat[0],
    sample_brazil['total_deaths'].median(),
    sample_brazil['total_deaths'].max() - sample_brazil['total_deaths'].min(),
    sample_brazil['total_deaths'].var(),
    sample_brazil['total_deaths'].std()
    ]

    sample_brazil['new_deaths_smoothed_per_million'] = pd.to_numeric(sample_brazil['new_deaths_smoothed_per_million'], errors='coerce')

    infos_total_deaths_smoothed = [
    sample_brazil['new_deaths_smoothed_per_million'].mean(),
    sample_brazil['new_deaths_smoothed_per_million'].mode().iat[0],
    sample_brazil['new_deaths_smoothed_per_million'].median(),
    sample_brazil['new_deaths_smoothed_per_million'].max() - sample_brazil['new_deaths_smoothed_per_million'].min(),
    sample_brazil['new_deaths_smoothed_per_million'].var(),
    sample_brazil['new_deaths_smoothed_per_million'].std()
    ]

    # Mesclar informações em um Dataframe
    dictInfos = {
    'Colunas': ['Total de Casos', 'Novos Casos', 'Novos Casos Suavizados', 'Obitos Recentes', 'Total de Obitos', 'Total de Obitos Suavizados'],
    'Media': [infos_total_cases[0], infos_new_cases[0], infos_new_cases_smoothed[0], infos_new_deaths[0], infos_total_deaths[0], infos_total_deaths_smoothed[0]],
    'Moda': [infos_total_cases[1], infos_new_cases[1], infos_new_cases_smoothed[1], infos_new_deaths[1], infos_total_deaths[1], infos_total_deaths_smoothed[1]],
    'Mediana': [infos_total_cases[2], infos_new_cases[2], infos_new_cases_smoothed[2], infos_new_deaths[2], infos_total_deaths[2], infos_total_deaths_smoothed[2]],
    'Amplitude': [infos_total_cases[3], infos_new_cases[3], infos_new_cases_smoothed[3], infos_new_deaths[3], infos_total_deaths[3], infos_total_deaths_smoothed[3]],
    'Variância': [infos_total_cases[4], infos_new_cases[4], infos_new_cases_smoothed[4], infos_new_deaths[4], infos_total_deaths[4], infos_total_deaths_smoothed[4]],
    'Desvio-Padrão': [infos_total_cases[5], infos_new_cases[5], infos_new_cases_smoothed[5], infos_new_deaths[5], infos_total_deaths[5], infos_total_deaths_smoothed[5]],
    }

    df_infos_brazil = pd.DataFrame(dictInfos)

    # vendo a correlação das colunas númericas da amostra do Brasil
    sample_brazil_corr = sample_brazil.drop(
        columns=['code', 'continent', 'country', 'date']
    )

    print(sample_brazil_corr.corr())

    # correlação em Mapa de Calor
    sns.heatmap(sample_brazil_corr.corr())
    plt.savefig(r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\images\sample_brazil_corr_map.png")

    # Plotando os dados no tempo
    fig = px.histogram(
        sample_brazil,
        title='Quantidade de Novos Casos de Covid-19 (Brasil)',
        labels={'date': 'Meses de 2020 a 2023', 'new_cases': 'Novos Casos'},
        x="date",
        y="new_cases"
    )

    # fig.update_layout(bargap=0.1)
    # fig.show()
    plt.savefig(r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\images\new_cases_brazil.png")

    fig = px.histogram(
        sample_argen,
        title='Quantidade de Novos Casos de Covid-19 (Argentina)',
        labels={'date': 'Meses de 2020 a 2023', 'new_cases': 'Novos Casos'},
        x="date",
        y="new_cases"
    )

    # fig.update_layout(bargap=0.1)
    # fig.show()
    plt.savefig(r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\images\new_cases_argen.png")

    fig = px.histogram(
        sample_chile,
        title='Quantidade de Novos Casos de Covid-19 (Chile)',
        labels={'date': 'Meses de 2020 a 2023', 'new_cases': 'Novos Casos'},
        x="date",
        y="new_cases"
    )

    # fig.update_layout(bargap=0.1)
    # fig.show()
    plt.savefig(r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\images\new_cases_chile.png")

    # Comparando os Novos Casos das amostras de Brasil, Argentina e Chile
    sns.set_theme(style="darkgrid")
    sns.lineplot(
        x="date",
        y="new_cases",
        hue="country",
        data=sampleMerged
    )
    # plt.show()

    # salvar graficos gerados
    plt.savefig(r"C:\Users\matutino\Documents\projects\BotCity\desafio07\assets\images\new_cases_countries.png")

    # images = [img01, img02, img03]
    # return images

data_analysis()