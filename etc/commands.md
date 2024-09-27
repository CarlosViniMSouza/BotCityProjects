0. Crie um venv (Opcional):

```bash
python -m virtualenv .venv
```

1. Atualizar cookiecutter:

```bash
python -m pip install --upgrade cookiecutter
```

2. Baixe e Selecione o Template: 

```bash
python -m cookiecutter https://github.com/botcity-dev/bot-python-template/archive/v2.zip
```

3. Informe o bot_id;

4. Entrar na pasta do projeto;

5. Digite o comando: 

```bash
conda create -n <name_project\> python=3.10 anaconda
```

6. Selecionar o ambiente virtual com python 3.10;

7. Entre na pasta do projeto e digite:

```bash
pip install -r requirements.txt
```

8. Instale o webdriver:

```bash
pip install webdriver_manager
```

9. Salvar as dependencias:

```bash
pip freeze > requirements.txt
```

- Para o lab

```bash
$ cd desafio07 && source venv/Scripts/activate && python src/main.py
```

```bash
$ pip install kaleido==0.1.0post1
```