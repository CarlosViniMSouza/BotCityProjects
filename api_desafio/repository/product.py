import database
import search_dolar as sd

def create_product(product):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        dolar_price_api = sd.search_dolar()
        
        sql = f"INSERT INTO product(description, unit, quantity, real_price, dolar_price) \
        VALUES('{product['description']}','{product['unit']}', '{product['quantity']}', '{product['real_price']}', '{dolar_price_api}')"
        cursor.execute(sql)

        last_id = cursor.lastrowid
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return last_id

def update_dolar_price(product):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        dolar_price_api = sd.search_dolar()

        sql = f"UPDATE product SET dolar_price = real_price / {dolar_price_api}"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()