# python3 -m venv .venv
# source .venv/bin/activate
# pip install mysql-connector-python
# deactivate

import conexao_mysql
import mysql.connector

class Deleta:

    def __init__(self, conexao):
        self.conexao = conexao


    def consultar(self, reg):

        try:
            conexao = conexao_mysql.Conexao.conectar_db(self)

            registro = str(reg)

            consulta_sql = 'SELECT * FROM professores WHERE registro = ' + registro
            cursor = conexao.cursor()
            cursor.execute(consulta_sql)

            linhas = cursor.fetchall()
            print('\nMostrando o professor: ')
            for linha in linhas:
                print('id: ', linha[0])
                print('nome: ', linha[1])
                print('preco: ', linha[2], '\n')

        except mysql.connector.Error as erro:
            print('\nFalha ao consultar a tabela no MySQL: {}'. format(erro))

        finally:
            conexao = conexao_mysql.Conexao.finalizar_conexao(self)


    def deletar(self, declaracao):
        try:
            conexao = conexao_mysql.Conexao.conectar_db(self)

            deletar_dados = declaracao
            cursor = conexao.cursor()
            cursor.execute(deletar_dados)
            conexao.commit()
            print('Exclusão efetuada com sucesso.')

        except mysql.connector.Error as erro:
            print('\nFalha ao excluir dados na tabela no MySQL: {}'. format(erro))

        finally:
            conexao = conexao_mysql.Conexao.finalizar_conexao(self)


    def alterar_dados(self):
        print('Ok')



if __name__ == '__main__':

    self = 'self'
    print('Excluir dados')

    print('\nDigite o código a ser excluído.')
    reg = input('Registro do professor: ')

    Deleta.consultar(self, reg)

    declaracao =    '''DELETE FROM professores
    WHERE registro = ''' + reg

    print(declaracao)
    Deleta.deletar(self, declaracao)
