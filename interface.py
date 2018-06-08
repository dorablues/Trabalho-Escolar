#   interface.py

#   import
from connection import *
#   vaiable

#   code
def clear():
    os.system('cls || clear')

def pause():
    os.system('pause')

class Display:
    '''Recursos de Interface'''
    value=None; alert='\t'

    def __init__(this,option):
        this.option=option

    ''''''
    def layout(this):
        '''Exibe o menu de contexto em uma janela de console'''
        leng=len(this.option)
        
        def exibe(limit):
            print('\t'+this.__class__.alert); print('\t'+'---'*10); print('\t'+this.option[0]); 
            for index in range(1,limit):
                print('\t'+('{}-{}').format(index,this.option[index]))
            print('\t'+'---'*10)
        #
        while True:
            #
            clear(); exibe(leng); this.__class__.value=''
            this.__class__.value=input('\tAbrir opção: ')
            #
            try:
                this.__class__.value=int(this.__class__.value)
                if this.__class__.value<1 or this.__class__.value>leng-1:
                    raise ValueError
                break
            except ValueError:
                if this.__class__.value=='':
                    this.__class__.alert=('Não pode ficar em branco. Tente de novo:')
                elif isinstance(this.__class__.value,str)==True:
                    this.__class__.alert=('Digite apenas números. Tente de novo:')
                else:
                    this.__class__.alert=('Opss, '+str(this.__class__.value)+' não está na lista. Tente de novo:')                   
        #
        return this.__class__.value
    #
    def message(cls):
        '''Retorna uma mensagem'''
        #
        print('\t'+cls.alert)
    '''    '''
    @classmethod
    def interface(cls):
        return cls.value, cls.alert

    if __name__=='__main__':
        form=Display(tuple)
        form.guide()
        form.message()