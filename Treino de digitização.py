# definir bloco de letras (ex: a,s l, e)

# criar aleatóriamente blocos de letras ( e dar respectivos espaços)

# imprimir blocos

import random
#from pyglet.window import key

print("Bem vindo ao seu treino de digitação." "\n"
        "Para sair do programa, tecle '9'" "\n")

                
def main():

    
    ''' Pede ao utilizador o nível o desejado'''
    def níveis():
        print ("Os níveis são:")
        print (" ")
        print ("iniciante_0 > 1)")
        print ("iniciante_1 > 2)")
        print ("iniciante_2 > 3)")
        print ("iniciante_3 > 4)")
        print (" ")
        return int(input("Escolha: "))

    choice = níveis()
    
    '''função que define o tamanho
        dos blocos de letras
    '''
    def digitação(choice):
        
        '''blocos de letras baseados na frequência
        na lingua Portuguesa'''

        bloco1=('a', 'e', 'o') 
        bloco2=('s', 'r', 'i')
        bloco3=('n', 'd', 'm', 'u', 't','c')
        bloco4=('l', 'p', 'v', 'g', 'h', 'q', 'b', 'f')
        bloco5=('z', 'j', 'x', 'k', 'w', 'y')
                
        def blocos_size(a=1, b=8):
            a = random.randint(a, b)
            #print(a)
            return a

        tamanho = blocos_size()

        '''
        função que imprime os blocos
        de letras mediante o tamanho definido
        pela função anterior e nível escolhido
        pelo utilizador
        '''
        def blocos_letras1(tamanho):
            for i in range(0, tamanho):
                if choice == 1:
                    bloco = random.choice(bloco1,bolco2)
                elif choice == 2:
                    bloco = random.choice(bloco2)
                elif choice == 3:
                    bloco = random.choice(bloco3)
                elif choice == 3:
                    bloco = random.choice(bloco3)
                elif choice == 4:
                    bloco = random.choice(bloco4)
                elif choice == 5:
                    bloco = random.choice(bloco5)
                print(bloco, end ='')
                
        print("Para sair do programa, tecle '9'")
        print("\n")
        
        blocos_letras1(tamanho)

        '''espera pelo "ENTER" para avançar
        o bloco seguinte ou pela tecla 9
        para sair do programa'''
               
        write= input('\n')
        if not write == "9":
            clear = "\n" * 100 # limpa a tela
            print(clear)       # limpa a tela
            digitação(choice)
        else:
            return
    
    digitação(choice)
                
            
main()
  