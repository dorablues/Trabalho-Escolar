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
    # instancia a classe Database e chama o metodo .new para criar uma nova tabela 
    db=Database('resource\dataBase.db'); db.new('CAD')
    # instancia a classe  Display com o argumento mainOption para gerar um menu 
    mainForm=Display(mainOption)
    # este laco de repeticao exibe o menu instanciado enquanto ele for verdade
    while True:
        # option recebe o conteudo da instancia mainForm que é instanciada com o 
        # metodo .layout()
        option=mainForm.layout()
        # se option receber 1 é iniciado uma nova instancia de Display para gerar
        # o proximo menu interativo
        if option==1:
            while True:
                # esta instancia representa o gerenciador de cadastros
                cadForm=Display(cadOption) # cadOption é a tupla que contem os labels de cadastros
                # agora option recebe o conteudo da instancia de cadForm sobrescrevendo
                # o conteudo de mainForm
                option=cadForm.layout()
                # se option receber 1 a tela será limpa paga configurar uma nova pagina 
                # de interacao com o usuario
                if option==1:
                    clear(); print('\n\t'+'---'*10); print('\t'+cadOption[1])
                    # este bloco faz a coleta dos dados atraves de input 
                    for i in range(4):
                        # tratamento de excecao de erro da variavel age
                        if label[i]=='IDADE':
                            while True:
                                try: # tentativa de coleta de idade
                                    age=int(input('\t'+label[i]+': '))
                                    # se a idade for menor que 1 ou maior do que 120
                                    # um erro sera gerado
                                    if age<1 or age>120:
                                        raise ValueError # levanta um tipo de erro chamado ValueError
                                    break # se a verificacao nao apresentar erro, o laco sera parado aqui
                                # neste bloco sera definido a mensagem de erro
                                except ValueError: 
                                    print('\tEsta não é uma idade válida!')
                        # os demais blocos seguem o mesmo padrao de operacao do bloco anterior
                        if label[i]=='ENDEREÇO':
                            while True:
                                try:
                                    address=input('\t'+label[i]+': ')
                                    if len(address)>50: #  neste caso se o input for maior do que 50 caracteres 
                                        # sera levantado um tipo de erro 
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('\tEste não é um endereço válido!')
                        # input para o nome de usuario
                        if label[i]=='NOME':
                            while True:
                                try:
                                    name=input('\t'+label[i]+': ')
                                    if len(name)==0: # esta verificacao procura saber se o nome esta vazio
                                        raise ValueError
                                    break
                                except ValueError:
                                    print('\tO nome não pode ficar em branco.')

                        # recebe salário
                        if label[i]=='SALÁRIO':
                            salary=float(input('\t'+label[i]+': '))                    
                    # cria uma tupla com as veriaveis coletadas
                    registro=(name,age,address,salary)
                    # instancia o banco de dados com os paramentros 'table' e 'row'
                    # table refere-se ao nome da tabela que o registros sera colocado
                    # row refere-se ao conteudo gravado no registro. row significa 'linha' ou 'registro' em ingles
                    db.insert(registro)
                    # exibe o que foi gravado
                    print('\n\t'+'Dados do formulário:')
                    print('\tNome: '+name)
                    print('\t'+str(age)+' anos')
                    print('\t'+address)
                    print('\tSalário: R$'+str(salary))
                    print('\n\n')
                    db.info() # chama o metodo .info na instancia 'db' da classe Database
                    print('\n\n'); pause() # exibe uma verificacao de concordancia antes de sair da pagina
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
            db.consulte(search)


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
