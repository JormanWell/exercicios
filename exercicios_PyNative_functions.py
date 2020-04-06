#https://pynative.com/python-functions-exercise-with-solutions/

# 1 ------------------------------------------

def name_age(name, age):
    print('Name', name, 'Age', age)
    
name_age('Jorge', 45)

# 2 ---------------------------------------

# devolve todos os argumentos duma função

def func1(*a):   # *a
    for i in a:
        print(i)
    
func1(20, 40, 60)

# 3 ---------------------------------

def calculation(a, b):
    return a+b, a-b
    
res = calculation(40, 10)
print(res)

# OU (retira os parentices):
add, sub = calculation(40, 10)
print(add, sub)

# 4 ----------------------------------------

def showEmployee(name, salary = 9000):
    print('Employee ', name, 'salary is:', salary)

showEmployee("Ben", 9000)
showEmployee("Ben")
# 5 ---------------------------------------

def multi(a, b):
    square = a**2
    
    def add(a, b):
        return square + b
    
    exp = add(a, b)
    return exp + 5

print(multi(5, 10))
# 6 ----------------------------------------

def sum0_10(a):
    a = list(range(a+1))
    
    b = 0
    for i in a:
        b = b + i
        
    print(b)
        
sum0_10(10)

# OU :

def calculateSum(num):
    if num:
        return num + calculateSum(num-1)
    else:
        return 0

res = calculateSum(10)
print(res)    
    
# 7 ---------------------------------

def displayStudent(name, age):
    print(name, age)

showStudent = displayStudent
showStudent("Emma", 26)

# 8 --------------------------
print(list(range(4, 40, 2)))

# 9 ----------------------------------

aList = [4, 6, 8, 24, 12, 2]

print(sorted(aList)[-1])
print(max(aList))
    
    
    
    
    
    
    
    
    
    
    
    
    
    