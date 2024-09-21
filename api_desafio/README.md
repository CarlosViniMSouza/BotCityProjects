# API Database

**Objetivo:** Desenvolver uma API com Flask e MySQL para gerenciar produtos.
    
**Instruções:**
    
1. **Criação do Ambiente de Desenvolvimento:**
    - Crie um ambiente virtual (venv) para o projeto.
    - Instale as bibliotecas necessárias para automação, extração dos dados e inserção de infos.

2. **Criação do Banco de Dados:**
    - Utilize o XAMPP para administrar o banco de dados.

3. **Testar as rotas:**
    - O `api_rest.http` contem todas as rotas a serem utilizadas (algumas precisam ser implementadas)

### **Instrução:**
    
- Crie e ative o ambiente virtual python

- Baixe as dependências do projeto

- Crie o banco de dados

### **Passo a Passo**

`OBS.: Verifique se o seu terminal está na pasta do projeto, isso é: (...)/BotCityProjects/api_desafio`

1. Crie e ative o ambiente virtual Python no seu terminal - será necessário para baixar as dependências:

- Recomendo a biblioteca [virtualenv](https://virtualenv.pypa.io/en/latest/product_guide.html), pois o conda tem me causado problemas.

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

## Rotas da Aplicação

### Funcionando no Momento

1. Criar produto:

- ROTA: (POST) http://127.0.0.1:5000/product

```json
{
  "description": "Mandioca",
  "unit": "Kg",
  "quantity": 20,
  "real_price": 500.0
}
```

### A implementar ...

2. Listar produtos criados:

- ROTA: (GET) http://127.0.0.1:5000/products

3. Obter produto pelo ID (numero '1' é um exemplo)

- ROTA: (GET) http://127.0.0.1:5000/product/14

4. Alterar produto pelo ID

- ROTA: (PUT) http://127.0.0.1:5000/product

```json
{
    "id": 14,
    "description": "Mandioca Especial",
    "unit": "Kg",
    "quantity": 40,
    "real_price": 600.0
}
```

5. Deletar produto pelo ID

- ROTA: (DEL) http://127.0.0.1:5000/product/1