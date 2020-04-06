# SLICE on STRINGS

# [START : STOP : STEP]

'0123456789'[0:3] # o 3 é exclusivo
# 012

'0123456789'[-1]  '0123456789'[-2] #-1 e -2 são INCLUSIVOS
# 9                # 8

'0123456789'[~1]   '0123456789'[~2]  #~1 e ~2 conta o índice pelo fim [0]
# 8

'0123456789'[1:~2]  #  o indice [0] está em ambas as pontas da lista
# 123456 

'0123456789'[0:-1]  '0123456789'[0:-2] # '01234567 ]8 ]9' -1 e -2 são EXCLUSIVOS
# 012345678         # 01234567

'0123456789'[:-7]     # '012 ] 3456789'[:-7] -7 é EXCLUSIVO 
# 012

'0123456789'[:-7:1] # salta  da esq, para a dir, um a um.
# 012

'0123456789'[:-7:2]  # salta da esq. para a dir, dois a dois
# 02

'0123456789'[:-7:-1]   # '012 [ 3456789' -7 é exclusivo. -1 inverte a ordem e salta uma a um.
# 987654

'0123456789'[:-7:-2]    # '012 [ 3456789' -7 é exclusivo. -1 inverte a ordem e salta 2 a dois.
# 975

'0123456789'[0:-7:-1]   # colocando 0 neste caso, não inverte a ordem e exclui todos os elementos
# ''




# .index() e .rindex() dá-nos a posição do carectér ou carectéres

data = '012A456789'
data.index('A')     # procuramos o índice do primeiro caractér (letra 'A' neste caso) 
# 3

data[3]
# 'A'

data2 = '012A45A6789'  # procura o índice da última ocurrência 
data2.rindex('A')
# 6

data2[6]
# 'A'

conjunto = data[:data.index('A')] # devolve todos os elementos até 'A' (EXCLUSIVO)
conjunto
# 012


# .find() (value, start, end)

data2 = '012A45A6789'
data2.find('A')     # procura o primeiro que encontrar
# 3

data2.find('A', 4)  # procura o primeiro que encontrar a partir do índice 4
# 6

data2.find('A', 2, 6) # procura o primeiro que encontrar a partir do índice 2 e finalisa
# 3                  # no índice 6 (EXCLUSIVO)

data2.find('A', 4, 4)  # se nada encontrar devolve -1
# -1

data2[data2.find('A', 2)+1 :data2.find('A', 5)] # selecionar entre os caractéres
# 45


# SLICE ON LISTS

lista = ['maça', 45, 'massa', 'arroz']

# indice devolve o mesmo dada type dos elementos da lista
lista[0] # 'maça'
lista[1] # 45
lista[3] # 'arroz'
lista[-2] # 'massa'

# slice devolve lista
lista[:-1] # ['maça', 45, 'massa']

lista[::-1] # ['arroz', 'massa', 45, 'maça']





