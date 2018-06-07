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


    def insert(this,table,row):
        ''' '''
        this.__class__.value=sqlite3.connect(this.database)
        
        this.__class__.value.execute('''INSERT INTO '''+table+''' (NAME,AGE,ADDRESS,SALARY) \
                VALUES (?,?,?,?)''',row)

        this.__class__.value.commit()


    def consulte(this,table,id):
        '''Returna os dados de uma pesquisa no banco de dados'''
        #

        def read():
            #
            sql = 'SELECT * FROM '+table+' ORDER BY nome'
            r = self.db.cursor.execute(sql)
            return r.fetchall()

        def show():
            #
            lista = self.ler_todos_clientes()
            print('{:>3s} {:20s} {:<5s} {:15s} {:21s} {:14s} {:15s} {:s} {:s}'.format(
                'id', 'nome', 'idade', 'cpf', 'email', 'fone', 'cidade', 'uf', 'criado_em'))

            for c in lista:
                print('{:3d} {:23s} {:2d} {:s} {:>25s} {:s} {:15s} {:s} {:s}'.format(
                    c[0], c[1], c[2],
                    c[3], c[4], c[5],
                    c[6], c[7], c[8]))




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