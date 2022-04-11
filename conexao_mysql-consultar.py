# python3 -m venv .venv
# source .venv/bin/activate
# pip install mysql-connector-python
# deactivate

import conexao_mysql
import mysql.connector

class Consultas:

    def __init__(self, conexao):
        self.conexao = conexao


    def consultar_tabela(self):

        try:            
            conexao = conexao_mysql.Conexao.conectar_db(self)

            consulta_sql = 'SELECT * FROM professores'
            cursor = conexao.cursor()
            cursor.execute(consulta_sql)

            linhas = cursor.fetchall()
            qtde = len(linhas)
            print('\nNúmero total de registro(s) encontrado(s): ', qtde)
            print('\nMostrando os professores: ')
            for linha in linhas:
                print('id: ', linha[0])
                print('nome: ', linha[1])
                print('preco: ', linha[2], '\n')

        except mysql.connector.Error as erro:
            print('\nFalha ao acessar a tabela no MySQL: {}'. format(erro))

        finally:
            conexao = conexao_mysql.Conexao.finalizar_conexao(self)


self = 'self'
Consultas.consultar_tabela(self)
