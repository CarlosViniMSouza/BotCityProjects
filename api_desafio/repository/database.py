import mysql.connector 

def create_db():
    try:
        mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='banco_desafio'
        )

    except Exception as ex:
        print(f'Error: {ex}')

    return mydb