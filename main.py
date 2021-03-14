import pyodbc
from uf import uf
from cidade import cidade
from distrito import distrito
from datetime import date, datetime

class Conexoes(object):

    def database_Azure(self):
        try:
            print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Iniciando conexão com o banco de dados no Azure...")
            conexao = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=sqlserver2134575.database.windows.net;'
                        'Database=conectividade-com-IBGE;'
                        'UID=sqluser;'
                        'PWD=Licesa@123;')
            print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Conexão realizada com sucesso com o banco de dados!\n")            
            cursor = conexao.cursor()
            print('1º carga: UF')
            uf(cursor)
            print('2º carga: Cidade')
            cidade(cursor)
            print('3º carga: Distrito')
            distrito(cursor)
        except Exception as error:
            print(f"{datetime.now().strftime('%H:%M:%S')}: "
              f"Não foi possível se conectar com o banco de dados...")
        pass
    pass


if __name__ == '__main__':

    caminho = Conexoes()
    caminho.database_Azure()