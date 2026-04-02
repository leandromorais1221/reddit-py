from mysql.connector import connect

class Conexao:
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "",
            "database": "mysql_reddit",
        }
    
    def obter_conexao(self):
        return connect(**self.config)
