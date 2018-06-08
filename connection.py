#   connection.py

#   import
import os; import sqlite3
#   vaiable

#   code

class Database:
    '''Recursos de database'''
    value=None; message=''

    def __init__(this,database):
        ''' '''
        this.database=database
        this.__class__.value=sqlite3.connect(database)
        # não utilizado
        this.__class__.content=None

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
            this.__class__.message='A tabela '+table+' foi criada no banco de dados'
        except sqlite3.OperationalError:
            this.__class__.message='A tabela '+table+' já existe neste banco de dados'


    def insert(this,table,row):
        ''' '''
        this.__class__.value=sqlite3.connect(this.database)
        
        this.__class__.value.execute('''INSERT INTO '''+table+''' (NAME,AGE,ADDRESS,SALARY) \
                VALUES (?,?,?,?)''',row)
        this.__class__.value.commit()
        this.__class__.message=('Os dados foram salvos com sucesso')


    def consulte(this,table,id):
        '''Consulta em uma tabela de dados e retorna com um registro'''
        # a linha a seguir faz a conexão com o banco de dados
        this.__class__.value=sqlite3.connect(this.database)
        # reader é o cursor de leitura deste método
        reader = this.__class__.value.cursor()
        # content é uma lista com os dados de registro gerado por ID
        content=reader.execute('SELECT * FROM '+table+' WHERE id = ?', (id,))
        # esta linha ainda apresenta inconsistencia
        if content == None:
            print(this.__class__.message) # !!! não está funcionando !!!
        # exibe uma grade com os registros alinhados de forma organizada
        # favor, não alterar este bloco
        else:
            # pula duas linhas antes de exibir o conteúdo
            print('\t\t')
            # grade de exibicao, não alterar abaixo
            for block in content:
                print('\t#ID: {:<5} CLIENTE: {:<25}\
        {} \n\tIdade: {:>5} anos \n\
        Endereço: {} \n\
        Salário:  R${}'.format(block[0],block[1],('\n\t'+'==-='*10),block[2],block[3],block[4]))

    
    # este metodo exibe uma mensagem 
    def info(cls):
        print('\t'+cls.message)


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
        db.insert(str,tuple)
        db.consulte(str,int)