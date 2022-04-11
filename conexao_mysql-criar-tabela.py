# python3 -m venv .venv
# source .venv/bin/activate
# pip install mysql-connector-python
# deactivate

import conexao_mysql
import mysql.connector

class Tabelas:

    def __init__(self, conexao):
        self.conexao = conexao


    def criar_tabela_exemplo(self):

        try:
            criar_tabela_exemplo =  '''CREATE TABLE tbl_produtos (
                                    id BIGINT NOT NULL,
                                    nome VARCHAR(50) NOT NULL,
                                    preco FLOAT NOT NULL,
                                    PRIMARY KEY (id)
                                    )'''
            
            conexao = conexao_mysql.Conexao.conectar_db(self)
            cursor = conexao.cursor()
            cursor.execute(criar_tabela_exemplo)

            database = conexao.cursor()
            database.execute('select database();')
            nome_database = database.fetchone()
            print('\nConectado ao banco de dados: ', nome_database[0])
            print('Tabela de Produtos criada com sucesso!')

        except mysql.connector.Error as erro:
            print('\nFalha ao criar a tabela no MySQL: {}'. format(erro))

        finally:
            conexao = conexao_mysql.Conexao.finalizar_conexao(self)
