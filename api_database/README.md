# API Database

**Objetivo:** Desenvolver uma API com Flask e MySQL para gerenciar usuários e produtos.
    
**Instruções:**
    
1. **Criação do Ambiente de Desenvolvimento:**
    - Crie um ambiente virtual (venv) para o projeto.
    - Instale as bibliotecas necessárias para automação, download de arquivos e visualização de dados.

2. **Criação do Banco de Dados:**
    - Utilize o XAMPP para administrar o banco de dados.

3. **Testar as rotas:**
    - O `api_rest.http` contem todas as rotas a serem utilizadas (algumas precisam ser implementadas)

### **Instrução:**
    
- Crie e ative o ambiente virtual python

- Baixe as dependências do projeto

- Crie o banco de dados

### **Passo a Passo**

`OBS.: Verifique se o seu terminal está na pasta do projeto, isso é: (...)/BotCityProjects/api_database`

1. Crie e ative o ambiente virtual Python no seu terminal - será necessário para baixar as dependências:

- Recomendo a biblioteca [virtualenv](https://virtualenv.pypa.io/en/latest/user_guide.html), pois o conda tem me causado problemas.

```bash
$ python -m virtualenv venv # criar ambiente virtual (de nome 'venv')
```

```bash
$ source venv/Scripts/activate # ativar ambiente virtual
```

2. Feito o ambiente virtual, precisamos baixar as dependências do projeto, para isso, execute o comando:

```bash
$ pip install -r requirements.txt # agora é só aguardar o fim do processo
```

3. Com as dependências instaladas na `venv`, ative o Apache e o MySQL no XAMPP (estará com a porta `3306`)

4. Entre na pasta `service`: `$ cd service`

5. Agora é só executar o arquivo `service_api.py`:

```bash
$ flask --app service_api run # (coloque o --debug para ativar a função debug)
```

## Rotas Funcionando (No momento)

1. Criar usuário:

- ROTA: (POST) http://127.0.0.1:5000/user

```json
{
    "name": "Carlos Souza",
    "login": "carlos",
    "password": "admin123",
    "email": "carlos@gmail.com"
}
```

2. Listar usuários criados:

- ROTA: (GET) http://127.0.0.1:5000/users

3. Obter usuário pelo ID (numero '1' é um exemplo)

- ROTA: (GET) http://127.0.0.1:5000/user/1

4. Alterar usuário pelo ID

- ROTA: (PUT) http://127.0.0.1:5000/user

```json
{
  "id": 1,
  "name": "Carlos Vini. M. Souza",
  "login": "carlos",
  "email": "carlos@gmail.com",
  "password": "admin123"
}
```

5. Deletar usuário pelo ID

- ROTA: (DEL) http://127.0.0.1:5000/user/1

6. Criar produto

- ROTA: (POST) http://127.0.0.1:5000/product

```json
{
  "description" : "Arroz",
  "unit" : "Kg",
  "quantity" : 3,
  "real_price" : 5.60,
  "dolar_price": 25
}
```
