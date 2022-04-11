# python3 -m venv .venv
# source .venv/bin/activate
# pip install mysql-connector-python
# deactivate

import mysql.connector

class Conexao:

    def __init__(self, conexao):
        self.conexao = conexao


    def conectar_db(self):
        try:
            conexao = mysql.connector.connect(
                host='localhost', 
                database='escola', 
                user='root', 
                password='********')
            return conexao

        except mysql.connector.Error as erro:
            print('Falha ao conectar com o servidor no MySQL: {}'. format(erro))


    def finalizar_conexao(self):
        conexao = Conexao.conectar_db(self)
        if conexao.is_connected():
            cursor = conexao.cursor()
            cursor.close()
            conexao.close()
            return conexao
