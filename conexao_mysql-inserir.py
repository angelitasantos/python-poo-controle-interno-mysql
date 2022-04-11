# python3 -m venv .venv
# source .venv/bin/activate
# pip install mysql-connector-python
# deactivate

import conexao_mysql
import mysql.connector

class Adiciona:

    def __init__(self, conexao):
        self.conexao = conexao


    def inserir_dados(self):
        
        registro = input('Digite o registro: ')
        depto = input('Digite o departamento: ')
        contratacao = input('Digite a data da contratação: ')

        dados = registro + ',\'' + depto + '\',\'' + contratacao + '\')'
        declaracao = '''INSERT INTO professores (registro, depto, contratacao) VALUES ('''
        sql = declaracao + dados

        try:            
            conexao = conexao_mysql.Conexao.conectar_db(self)

            adiciona_sql = sql
            cursor = conexao.cursor()
            cursor.execute(adiciona_sql)
            conexao.commit()
            qtde = len(adiciona_sql)
            print(qtde)
            cursor.close()

        except mysql.connector.Error as erro:
            print('\nFalha ao inserir dados no MySQL: {}'. format(erro))

        finally:
            conexao = conexao_mysql.Conexao.finalizar_conexao(self)


self = 'self'
Adiciona.inserir_dados(self)
