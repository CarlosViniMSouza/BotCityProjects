# Desafio 07

**Objetivo:** Desenvolver um script em Python que automatize o processo de download de dados sobre COVID-19 a partir de um site específico, salve os dados em um arquivo local e gere um gráfico a partir desses dados. O desafio envolve acessar um site confiável de estatísticas sobre COVID-19, baixar os dados mais recentes, processá-los e visualizar as informações por meio de um gráfico. No final gere um relatório em excel.

- https://covid.ourworldindata.org
    
**Instruções:**
    
1. **Criação do Ambiente de Desenvolvimento:**
    - Crie um ambiente virtual (venv) para o projeto.
    - Instale as bibliotecas necessárias para automação, download de arquivos e visualização de dados.

2. **Automatização do Download de Dados:**
    - Utilize Python para acessar um site de estatísticas sobre COVID-19 e baixar os dados mais recentes (por exemplo, em formato CSV).

3. **Processamento e Visualização dos Dados:**
    - Leia o arquivo baixado, processe os dados relevantes e crie um gráfico que mostre, por exemplo, a evolução diária de casos ou mortes.
    
4. **Execução e Testes:**
    - Execute o script para garantir que os dados são baixados corretamente e que o gráfico é gerado com precisão.

### **Instrução:**
    
- Configure e execute o script para garantir que os dados COVID-19 são baixados corretamente e que o gráfico é gerado com precisão.

- Experimente filtrar os dados para diferentes países ou regiões e criar gráficos adicionais para análise comparativa.

- Teste o script com diferentes intervalos de tempo e variáveis (como novos casos, novas mortes, vacinação, etc.).

### **Passo a Passo**

`OBS.: Verifique se o seu terminal está na pasta do projeto, isso é: (...)/BotCityProjects/desafio07`

1. Crie e ative o ambiente virtual Python no seu terminal - será necessário para baixar as dependências:

- Recomendo a biblioteca [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html), pois o conda tem me causado problemas.

```bash
$ python -m virtualenv venv # criar ambiente virtual
```

```bash
$ source venv/Scripts/activate # ativar ambiente virtual
```

2. Feito o ambiente virtual, precisamos baixar as dependências do projeto, para isso, execute o comando:

```bash
$ pip install -r requirements.txt # agora é só aguardar o fim do processo
```

3. Com as dependências instaladas na `venv`, basta executar o arquivo principal `main.py`:

```bash
$ python main.py
```

## Agora é só esperar o Python fazer as tarefas a serem feitas! 🚀
