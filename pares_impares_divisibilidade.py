# COMPARADOR PAR/IMPAR E DIVISIBILIDADE

num = int(input("Hi there! Give me a number!"))
check = int(input("Give a check number if it is divisivel by first one!"))
                  
if num % check == 0:
    print(num, "devides envenly by", check)
else:
    print(num, "does not divide evenly by", check)

if num % 4 == 0:
    print('The number', num, 'is a multiple of 4 and is even.')
elif num % 2 == 0:
    print('The number that you gave me,', num, ' is even.')
else:
    print('The number that you gave me,', num, 'is odd.')
