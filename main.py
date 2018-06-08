#   main.py

#   import
from interface import *
from connection import Database
#   vaiable
mainOption=('Guia Principal','Gerenciar Cadastro','Consultar Cadastro','Sobre o programa','Sair do programa')
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
                    clear(); print('\n\t'+'---'*10); print('\t'+cadOption[1])
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
                            while True:
                                try:
                                    name=input('\t'+label[i]+': ')
                                    if len(name)==0:
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('\tO nome não pode ficar em branco.')

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
        #   Consulta de cadastro no banco de dados
        elif option==2:
            # a linha a seguir limpa a tela e exibre o label de titulo da funcao 'Consular cadastro'
            clear(); print('\n\t'+'---'*10); print('\t'+mainOption[2])
            search=int(input('\tDigite o id: '))
            db.consulte('CAD',search)


            # saida da funcao
            print('\n\n'); pause()
        elif option==3:
            clear(); print('\n\t'+'---'*10); print('\t'+mainOption[3])
            print('\n\tTrabalho acadêmico do curso técnico de Informática\n\tDiciplina: Técnicas de Programação sobre ministração de Lucineia \n\n')

            print('\tIntegrantes: \n\n\t1-Jhonatan Almeida \n\t2-João Mateus \n\t3-Larissa \n\t4-Rebeca')

            print('\n\n'); pause()
        elif option==4:
            break




main()