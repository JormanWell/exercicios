# definir bloco de letras (ex: a,s l, e)

# criar aleatóriamente blocos de letras ( e dar respectivos espaços)

# imprimir blocos

import random

print("Bem vindo ao seu treino de digitação." "\n"
        "Para sair do programa, tecle '9'" "\n")

                
def main():
        
    '''blocos de letras baseados na frequência
    na lingua Portuguesa'''

    bloco1=('a', 'e', 'o') 
    bloco2=('s', 'r', 'i')
    bloco3=('n', 'd', 'm', 'u', 't','c')
    bloco4=('l', 'p', 'v', 'g', 'h', 'q', 'b', 'f')
    bloco5=('z', 'j', 'x', 'k', 'w', 'y')
        
    ''' Pede ao utilizador o nível n desejado'''
    def níveis():
        print ("Os níveis são:")
        print (" ")
        print ("1) iniciante_0")
        print ("2) iniciante_1")
        print ("3) iniciante_2")
        print ("4) iniciante_3")
       # print ("5) Quit calculator.py")
        print (" ")
        return int(input("Escolha: "))

    choice = níveis()
    if choice == 1:
    '''elif choice == 2:
        blocos_letras1(a)
        #loop = 0
    elif choice == 3:
        blocos_letras1(a)
        #loop = 0
    elif choice == 4:
        blocos_letras1(a)
        #loop = 0
    elif choice == 5:
        #loop = 0'''
          

    '''função que define o tamanho
        dos blocos de letras
    '''
    
    def blocos_size(a=1, b=8):
        a = random.randint(a, b)
        #print(a)
        return a

    a = blocos_size()

    '''
    função que imprime os blocos
    de letras mediante o tamanho definido
    pela função anterior
    '''
    def blocos_letras1(a):
        for i in range(0, a):
            bloco = random.choice(bloco1)
            print(bloco, end ='')
        
    blocos_letras1(a)

    '''espera pelo "ENTER" para avançar
    o bloco seguinte ou pela tecla 9
    para sair do proggrama'''
    
    
        blocos_letras1(a)
            
            
    write= input('\n')
    if not write == "9":
        main()
            
                
            
main()