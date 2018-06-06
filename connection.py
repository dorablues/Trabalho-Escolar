#   connection.py

#   import
import os; import sqlite3
#   vaiable

#   code

class Database:
    '''Recursos de database'''
    value=None; alert=''

    def __init__(this,database):
        ''' '''
        this.database=database
        this.__class__.value=sqlite3.connect(database)
    ''' metodos de funcao '''
    def new(this,table):
        '''Cria uma nova tabela em um banco de dados'''
        this.__class__.value=sqlite3.connect(this.database)
        try:
            this.__class__.value.execute('''CREATE TABLE '''+table+''' (
                   ID INTEGER     PRIMARY KEY     AUTOINCREMENT,
                   NAME           TEXT            NOT NULL,
                   AGE            INT             NOT NULL,
                   ADDRESS        CHAR(50),
                   SALARY         REAL);''')
            this.__class__.alert='A tabela '+table+' foi criada no banco de dados'
        except sqlite3.OperationalError:
            this.__class__.alert='A tabela '+table+' já existe neste banco de dados'

    def consulte(this,id):
        '''Returna os dados de uma pesquisa no banco de dados'''

        this.__class__.value=sqlite3.connect(this.database)

        this.__class__.value.execute("")

        this.__class__.alert='A tabela '+table+' foi criada no banco de dados'



    def status(cls):
        print(cls.alert)
    ''' metodos da classe'''    
    @classmethod
    def connection(cls):
        ''' '''
        return cls.value, cls.alert

    if __name__=='__main__':
        db=Database(str)
        db.new(str)
        db.status()