from mysql.connector import connect

def obter_conexao():
    try:
        config = {
            "host": "",
            "database": "",
            "user": "",
            "password": ""
        }
        return connect(**config)
    except Exception as error:
        print("Erro ao conectar com o banco de dados!", error)