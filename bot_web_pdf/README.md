# API Database

**Objetivo:** Desenvolver uma API com Flask e MySQL para gerenciar produtos e usuários.
    
**Instruções:**
    
1. **Criação do Ambiente de Desenvolvimento:**
    - Crie um ambiente virtual (venv) para o projeto.
    - Instale as bibliotecas necessárias para automação, extração dos dados e inserção de infos.

2. **Criação do Banco de Dados:**
    - Utilize o XAMPP para administrar o banco de dados.

3. **Testar as rotas:**
    - O `api_rest.http` **NÃO CONTEM** todas as rotas a serem utilizadas (algumas precisam ser implementadas)

### **Instrução:**
    
- Crie e ative o ambiente virtual python

- Baixe as dependências do projeto

- Crie o banco de dados

- Acione a API do projeto

_ Execute o bot do Excel

### **Passo a Passo**

1. Crie o banco de dados `bank_bot_web_pdf` no XAMPP (use o `script.sql` para isso!)

2. Utilize o cookiecutter (p/ atualizar a lib):

```bash
$ python -m pip install --upgrade cookiecutter
```

3. Baixe o template do bot para Web:

```bash
$ python -m cookiecutter https://github.com/botcity-dev/bot-python-template/archive/v2.zip
```

4. Escolha a opção '2 - (Web)' e dê um nome para o projeto (Ex.: botproduto)

5. Crie o ambiente virtual:

- conda: `conda create --name conda_web_pdf python=3.10`

- virtualenv: `python -m virtualenv venv`

6. Instale as dependências:

```bash
pip install -r requirements.txt
```

7. Acione a API

```bash
$ python api/api.py
```

8. Se tudo deu certo, acione o bot:

```bash
$ python main.py
```
