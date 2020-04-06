# devolve-nos os numeros ímpares

entrada = int(input("nº "))
numero = entrada + 1      # passa a incluir o último objecto

list(range(1,numero, 2))

for i in range(1, numero, 2):      
    print(i, end=' ') 
