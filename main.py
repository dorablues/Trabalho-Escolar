#   main.py

#   import
from interface import *
from connection import Database
#   vaiable
mainOption=('Guia Principal','Gerenciar Cadastro','Consultar Cadastro','Sobre os desenvolvedores','Sair do programa')
cadOption=('Guia Principal > Gerenciar Cadastro','Novo Cadastro','Alterar cadastro','Excluir cadastro','Voltar Para a Guia Principal')
label=('NOME','IDADE','ENDEREÇO','SALÁRIO')
#   code
def main():
    db=Database('dataBase.db'); db.new('CAD')
    #
    mainForm=Display(mainOption)
    #
    while True:
        #
        option=mainForm.layout()
        #
        if option==1:
            while True:
                #
                cadForm=Display(cadOption)
                #
                option=cadForm.layout()
                #
                if option==1:
                    clear(); print('\n\t'+'---'*10); print('\tNOVO CADASTRO: ')
                    #
                    for i in range(4):
                        #
                        if label[i]=='IDADE':
                            while True:
                                try:
                                    age=int(input('\t'+label[i]+': '))
                                    if age<1 or age>120:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('\tEsta não é uma idade válida!')
                        #
                        if label[i]=='ENDEREÇO':
                            while True:
                                try:
                                    address=input('\t'+label[i]+': ')
                                    if len(address)>50:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('\tEste não é um endereço válido!')
                        #
                        if label[i]=='NOME':
                            name=input('\tNOME: ')
                        #
                        if label[i]=='SALÁRIO':
                            salary=float(input('\t'+label[i]+': '))                    
                    #
                    registro=(name,age,address,salary)
                    #
                    db.insert('CAD',registro)
                    #
                    print('\t'+name)
                    print('\t'+str(age))
                    print('\t'+address)
                    print('\t'+str(salary))
                    db.info()
                    print('\n\n'); pause()
                elif option==2:
                    pass
                elif option==3:
                    pass
                elif option==4:
                    break
        elif option==2:
            pass
        elif option==3:
            pass
        elif option==4:
            break




main()