#EXERCÍCIO 3
#Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:

# 1. Instead of printing the elements one by one, make a new list that has all the elements
#    less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original list
#    a that are smaller than that number given by the user.

# --------------------- START----------------------------------------------
a = [1, 53, 1, 2, 3, 89, 8, 5, 13, 21, 34]  # uma lista desordenada
# Exercicio 1.1

print(list(a[:4] + a[5:]))  # imprime a lista retirando o índice 4
assert isinstance(a, object)
print(a)

# Exercicio 1.2
num = int(input("Give me a number from the list:" "\n"))
a_ = sorted(a)                                              #ordena a lista
ind_num = print(list(a_[:a_.index(num)]))           #imprime e lista até ao numero do dado em "input"

# Exercício 1.3

#imprime os numeros um a um                

for numero in a_:
    if numero < num:
        print(numero)

# O mesmo efeito exercício 1.2

ind_num_2 = a_.index(num)

for numero in a_:       
    if num > numero:
        print(a_[:ind_num_2])
        break

