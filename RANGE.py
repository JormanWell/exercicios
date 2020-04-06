""" RANGE()
 LINKS ÚTEIS
 https://pynative.com/python-range-function/

 range (start, stop[, step]) """

for i in range(3):
    print(i)
# 0
# 1
# 2

for i in range(3):
    print(list,(i)) #lista cada um dos objectos
# <class 'list'> 0
# <class 'list'> 1
# <class 'list'> 2

for i in range(3, 7):
    print(i, end=' ')    # end= coloca num só linha sepradado pelo que se entender
# 3 4 5 6

# ---------------------------------------------------------------------------------|
start = 0
stop = 7
step = 1
stop += step

for i in range(start, stop, step):      # passa a incluir o último objecto
    print(i, end=' ')    
# 3 4 5 6
# ---------------------------------------------------------------------------------|

for i in range(1, 12, 1):
    print(i, end=' ')    # slata de 2 em 2 passos, exclui o primeiro (NÃO PODE SER 0)
# 3 4 5 6 1 3 5 7 9 11

for i in range(12, 2, -1):
    print(i, end=' ')    # coloca de forma descendente
# 12 11 10 9 8 7 6 5 4 3 

for i in range(-2, 5, 1):
    print(i, end=", ")      # Dá-nos de um número negativo a positivo
# -2, -1, 0, 1, 2, 3, 4,

range(2,8)[3]               # tal como numa lista, é possível indexar ou fazer "slice"
# 5 

for i in range(10, 100):
   # if i % 4 == 0:
        print(i, end=' ') # dá-nos todos os números divisiveis por 4 entre 10 e 100
# 12 16 20 24 28 32 36 40 44 48 52 56 60 64 68 72 76 80 84 88 92 96 

# CONVERTER EM UMA LISTA OS OBJECTOS DE RANGE()

listB = list( range(2, 10, 2))
print("printing list", listB)
#[2, 4, 6, 8]



