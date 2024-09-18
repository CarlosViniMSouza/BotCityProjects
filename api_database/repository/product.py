import dadabase 

def create_product(produto):
    try:
        # Manipular o banco de dados
        conect = dadabase.criar_db()
        cursor = conect.cursor()

        sql = f"INSERT INTO produto(descricao, unidade, quantidade, preco_real, preco_dolar) VALUES('{produto['descricao']}','{produto['unidade']}', '{produto['quantidade']}', '{produto['preco_real']}','{produto['preco_dolar']}')"

        print(sql)
        
        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()
    except Exception as ex:
        print(f'Erro: Falha na inclusão: {ex}')

    return last_id 
