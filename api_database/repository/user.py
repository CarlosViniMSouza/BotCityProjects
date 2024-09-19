import database 

# Verificar se Usuario existe
def check_user_exists(id):
    exists: False

    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM user WHERE id = '{id}'"
        
        cursor.execute()
        list_users = cursor.fetchall()
        
        if len(list_users) == 0:
            exists = False
        else:
            exists = True

    except Exception as ex:
        print(f'Erro: {ex}')

    return exists

# Add Usuario com as devidas informações
def create_user(user):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"INSERT INTO user(name, login, password, email) VALUES('{user['name']}','{user['login']}', '{user['password']}', '{user['email']}')"

        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return last_id

# Fornecer lista de Usuarios
def list_users():
    users = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM user ORDER BY name'

        cursor.execute(sql)
        list_users = cursor.fetchall()

        for user in list_users:
            users.append({
                'id': user[0],
                'name': user[1],
                'login': user[2],
                'password': user[3],
                'email': user[4]
            })

    except Exception as ex:
        print(f'Erro: Listar user: {ex}')

    finally:
        cursor.close()
        conect.close()

    return users

# Buscar Usuario pelo ID
def get_user_id(id):
    users = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM user WHERE id = '{id}'"

        cursor.execute(sql)
        list_users = cursor.fetchall()

        for user in list_users:
            users.append({
                'id': user[0],
                'name': user[1],
                'login': user[2],
                'password': user[3],
                'email': user[4]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return users

# Atualizar infos cadastradas
def update_user(user):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"UPDATE user SET name = '{user['name']}', login = '{user['login']}', password = '{user['password']}', email = '{user['email']}' WHERE id = '{user['id']}'"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

# Remover Usuario
def delete_user(id):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM user WHERE id = {id}'

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()
