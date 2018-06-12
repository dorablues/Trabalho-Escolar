#   connection.py

#   import
import os; import sqlite3
#   vaiable

#   code

class Database:
    '''Recursos de database'''
    value=None; message=''

    def __init__(this,database):
        '''Conexão com o banco de dados'''
        this.database=database # grava o nome do banco de dados para uso posterior
        # a linha a seguir faz uma conexão com o banco de dados
        while True:
            try:
                this.__class__.value=sqlite3.connect(database)
                break
            except sqlite3.OperationalError:
                if os.path.exists('resource')==False:
                    os.makedirs('resource')
        # 
        this.table=None
        this.row=None
        this.id=None
        this.__class__.content=None

    ''' metodos de funcao '''
    def new(this,table):
        '''Cria uma nova tabela em um banco de dados'''
        this.table=table
        # a linha a seguir faz a conexão com o banco de dados
        this.__class__.value=sqlite3.connect(this.database)
        # tenta criar uma nova tabela no banco de dados e se ela já existir
        # retorna um erro de que a tabela já existe
        try:
            this.__class__.value.execute('''CREATE TABLE '''+this.table+''' (
                   ID INTEGER     PRIMARY KEY     AUTOINCREMENT,
                   NAME           TEXT            NOT NULL,
                   AGE            INT             NOT NULL,
                   ADDRESS        CHAR(50),
                   SALARY         REAL);''')
            # grava a mensagem de sucesso no atributo message
            this.__class__.message='A tabela '+this.table+' foi criada no banco de dados'
        # except retorna um erro de que a tabela nao pode ser criada
        except sqlite3.OperationalError:
            # grava a mensagem de erro no arributo message
            this.__class__.message='A tabela '+this.table+' já existe neste banco de dados'

    def insert(this,row):
        '''Insere registros em uma tabela de banco de dados'''
        this.row=row
        # a linha a seguir faz a conexão com o banco de dados
        this.__class__.value=sqlite3.connect(this.database)
        # executa a funcao query 'INSERT INTO' e insere os dados na tabela
        this.__class__.value.execute('''INSERT INTO '''+this.table+''' (NAME,AGE,ADDRESS,SALARY) \
                VALUES (?,?,?,?)''',this.row)
        this.__class__.value.commit() # salva os dados gravados
        this.__class__.message=('Os dados foram salvos com sucesso') # grava a mensagem de sucesso no atributo message


    def consulte(this,id):
        '''Consulta em uma tabela de dados e retorna com um registro'''
        this.id=id
        # a linha a seguir faz a conexão com o banco de dados
        this.__class__.value=sqlite3.connect(this.database)
        # reader é o cursor de leitura deste método
        reader = this.__class__.value.cursor()
        # content é uma lista com os dados de registro gerado por ID
        this.content=reader.execute('SELECT * FROM '+table+' WHERE id = ?', (this.id,))
        # esta linha ainda apresenta inconsistencia
        if this.content == None:
            print(this.__class__.message) # !!! não está funcionando !!!
        # exibe uma grade com os registros alinhados de forma organizada
        # favor, não alterar este bloco
        else:
            # pula duas linhas antes de exibir o conteúdo
            print('\t\t')
            # grade de exibicao, não alterar abaixo
            for block in this.content:
                print('\t#ID: {:<5} CLIENTE: {:<25}\
        {} \n\tIdade: {:>5} anos \n\
        Endereço: {} \n\
        Salário:  R${}'.format(block[0],block[1],('\n\t'+'==-='*10),block[2],block[3],block[4]))

    
        # executa a funcao sql UPDATE, esta funcao atualiza um registro
    # este metodo exibe uma mensagem 
    def info(cls):
        print('\t'+cls.message)


    def status(cls):
        '''Retorna a mensagem da classe'''
        print(cls.message)
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