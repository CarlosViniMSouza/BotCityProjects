import database 

# Verificar se eleitor existe
def check_voter_exists(cpf):
    exists: False

    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"SELECT * FROM voter WHERE cpf = '{cpf}'"
        
        cursor.execute()
        list_voters = cursor.fetchall()
        
        if len(list_voters) == 0:
            exists = False
        else:
            exists = True

    except Exception as ex:
        print(f'Erro: {ex}')

    return exists

# Add eleitor com as devidas informações
def create_voter(voter):
    try:
        conect = database.create_db()
        cursor = conect.cursor()

        # sql = f"INSERT INTO voter(cpf, nome, data_nascimento, nome_mae, cep, nro_endereco, nro_titulo, situacao, secao, zona, local_votacao, endereco_votacao, bairro, municipio_uf, pais) VALUES('{voter['cpf']}','{voter['nome']}', '{voter['data_nascimento']}', '{voter['nome_mae']}', '{voter['cep']}', '{voter['nro_endereco']}', '{voter['nro_titulo']}', '{voter['situacao']}', '{voter['secao']}', '{voter['zona']}', '{voter['local_votacao']}', '{voter['endereco_votacao']}', '{voter['bairro']}', '{voter['municipio_uf']}', '{voter['pais']}')"

        sql = f"INSERT INTO voter(cpf, nome, data_nascimento, nome_mae, cep, nro_endereco) VALUES('{voter['cpf']}','{voter['nome']}', '{voter['data_nascimento']}', '{voter['nome_mae']}', '{voter['cep']}', '{voter['nro_endereco']}')"

        cursor.execute(sql)
        last_cpf = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return last_cpf

# Fornecer lista de eleitores
def list_voters():
    voters = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM voter ORDER BY nome'

        cursor.execute(sql)
        list_voters = cursor.fetchall()

        for voter in list_voters:
            # voters.append({
            #     'cpf': voter[0],
            #     'nome': voter[1],
            #     'data_nascimento': voter[2],
            #     'nome_mae': voter[3], 
            #     'cep': voter[4], 
            #     'nro_endereco': voter[5],
            #     'nro_titulo': voter[6], 
            #     'situacao': voter[7], 
            #     'secao': voter[8], 
            #     'zona': voter[9],
            #     'local_votacao': voter[10], 
            #     'endereco_votacao': voter[11], 
            #     'bairro': voter[12],
            #     'municipio_uf': voter[13], 
            #     'pais': voter[14]
            # })

            voters.append({
                'cpf': voter[0],
                'nome': voter[1],
                'data_nascimento': voter[2],
                'nome_mae': voter[3], 
                'cep': voter[4], 
                'nro_endereco': voter[5]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return voters

# Buscar eleitor pelo cpf
def get_voter_cpf(cpf):
    voters = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM voter WHERE cpf = '{cpf}'"

        cursor.execute(sql)
        list_voters = cursor.fetchall()

        for voter in list_voters:
            # voters.append({
            #     'cpf': voter[0],
            #     'nome': voter[1],
            #     'data_nascimento': voter[2],
            #     'nome_mae': voter[3], 
            #     'cep': voter[4], 
            #     'nro_endereco': voter[5],
            #     'nro_titulo': voter[6], 
            #     'situacao': voter[7], 
            #     'secao': voter[8], 
            #     'zona': voter[9], 
            #     'local_votacao': voter[10], 
            #     'endereco_votacao': voter[11], 
            #     'bairro': voter[12],
            #     'municipio_uf': voter[13], 
            #     'pais': voter[14]
            # })

            voters.append({
                'cpf': voter[0],
                'nome': voter[1],
                'data_nascimento': voter[2],
                'nome_mae': voter[3], 
                'cep': voter[4], 
                'nro_endereco': voter[5]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return voters

# Atualizar infos cadastradas
def update_voter(voter):
    try:
        conect = database.create_db()
        cursor = conect.cursor()

        # sql = f"UPDATE voter SET cpf = '{voter['cpf']}', nome = '{voter['nome']}', data_nascimento = '{voter['data_nascimento']}', nome_mae = '{voter['nome_mae']}', cep = '{voter['cep']}', nro_endereco = '{voter['nro_endereco']}', nro_titulo = '{voter['nro_titulo']}', situacao = '{voter['situacao']}', secao = '{voter['secao']}', zona = '{voter['zona']}', local_votacao = '{voter['local_votacao']}', endereco_votacao = '{voter['endereco_votacao']}', bairro = '{voter['bairro']}', municipio_uf = '{voter['municipio_uf']}', pais = '{voter['pais']}' WHERE cpf = '{voter['cpf']}'"

        sql = f"UPDATE voter SET cpf = '{voter['cpf']}', nome = '{voter['nome']}', data_nascimento = '{voter['data_nascimento']}', nome_mae = '{voter['nome_mae']}', cep = '{voter['cep']}', nro_endereco = '{voter['nro_endereco']}' WHERE cpf = '{voter['cpf']}'"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

# Remover eleitor
def delete_voter(cpf):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM voter WHERE cpf = {cpf}'

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()
