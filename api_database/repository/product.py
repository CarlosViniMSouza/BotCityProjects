import database 

def create_product(product):
    try:
        conect = database.create_db()
        cursor = conect.cursor()

        sql = f"INSERT INTO product(description, unit, quantity, real_price, dolar_price) VALUES('{product['description']}','{product['unit']}', '{product['quantity']}', '{product['real_price']}','{product['dolar_price']}')"

        print(sql)

        cursor.execute(sql)
        last_id = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    return last_id 