import database 

# Verificar se Usuário existe
def check_user_exists(id):
    existe: False
    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM user WHERE id = '{id}'" 
        cursor.execute()
        list_user = cursor.fetchall()
        if len(list_user) == 0:
            existe = False
        else:
            existe = True
    except Exception as ex:
        print(f'Erro na verificacao do user: {ex}')

    return existe

# Fornecer lista de usuários
def list_users():
    users = list()
    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM user ORDER BY nome'
        cursor.execute(sql)
        list_user = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for user in list_user:
            users.append(
                {
                  'id': user[0],
                  'nome': user[1],
                  'login': user[2],
                  'senha': user[3],
                  'email': user[4]
                }
            )
    except Exception as ex:
        print(f'Erro: Listar user: {ex}')
    
    return users
# Fim: list_users() 

def get_user_id(id):
    users = list()
    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM user WHERE id = '{id}'" 
        cursor.execute(sql)
        list_user = cursor.fetchall()
        # Tratar dados para uma estrutura JSON
        for user in list_user:
            users.append(
                {
                  'id': user[0],
                  'nome': user[1],
                  'login': user[2],
                  'senha': user[3],
                  'email': user[4]
                }
            )
    except Exception as ex:
        print(f'Erro: obter user pelo id: {ex}')

    return users
# Fim: obter_user_id(id)

def create_user(user):
    try:
        # Manipular o banco de dados
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO user(nome, login, senha, email) VALUES('{user['nome']}','{user['login']}', '{user['senha']}', '{user['email']}')"
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')

    return last_id 
# Fim: create_user(user)


def update_user(user):
    try:
        # Manipular o banco de dados
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"UPDATE user SET nome = '{user['nome']}', login = '{user['login']}', senha = '{user['senha']}', email = '{user['email']}' WHERE id = '{user['id']}' "
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na atualização: {ex}')

# Fim: create_user(user)

def delete_user(id):
    try:
        # Manipular o banco de dados
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM user WHERE id = {id}'
        cursor.execute(sql)
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na deleção do user: {ex}')
# Fim: update_user




    