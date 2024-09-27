from repository import user
from repository import product
from repository import database
#import mysql.connector

version = "1.0.0"

def get_start():
    print(f"My package version {version} was started!")

# Executando a função de inicialização ao importar o pacote
get_start()

__all__ = ["repository"]
