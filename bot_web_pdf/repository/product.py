import database
import search_dolar as sd

# --- Para fins especificos

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

# --- Para fins especificos

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

# Fornecer lista de produtos
def list_products():
    products = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = 'SELECT * FROM product ORDER BY description'

        cursor.execute(sql)
        list_products = cursor.fetchall()

        for product in list_products:
            products.append({
                'id': product[0],
                'description': product[1],
                'unit': product[2],
                'quantity': product[3],
                'real_price': product[4],
                'dolar_price': product[5]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return products

# Buscar produto pelo ID
def get_product_id(id):
    products = list()

    try:
        conect = database.create_db()
        cursor = conect.cursor() 
        sql = f"SELECT * FROM product WHERE id = '{id}'"

        cursor.execute(sql)
        list_products = cursor.fetchall()

        for product in list_products:
            products.append({
                'id': product[0],
                'description': product[1],
                'unit': product[2],
                'quantity': product[3],
                'real_price': product[4],
                'dolar_price': product[5]
            })

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

    return products

# Atualizar produto
def update_product(product):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f"UPDATE product SET description = '{product['description']}', unit = '{product['unit']}', quantity = '{product['quantity']}', real_price = '{product['real_price']}' WHERE id = '{product['id']}'"

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()

# Deletar produto
def delete_product(id):
    try:
        conect = database.create_db()
        cursor = conect.cursor()
        sql = f'DELETE FROM product WHERE id = {id}'

        cursor.execute(sql)
        conect.commit()

    except Exception as ex:
        print(f'Erro: {ex}')

    finally:
        cursor.close()
        conect.close()