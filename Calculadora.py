def menu():
    # print what options you have
    print ("Welcome to calculator.py")
    print ("your options are:")
    print (" ")
    print ("1) Addition")
    print 	
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator.py")
    print (" ")
    return int(input("Choose your option: "))

# this adds two numbers given
def add(a, b):
    print (a, "+", b, "=", a + b)

# this subtracts two numbers given
def sub(a, b):
    print (b, "-", a, "=", b - a)

# this multiplies two numbers given
def mul(a, b):
    print (a, "*", b, "=", a * b)

# this divides two numbers given
def div(a, b):
    print (a, "/", b, "=", a / b)

# NOW THE PROGRAM REALLY STARTS, AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
         add(a=int(input("Add this: ")), b=int(input("to this: ")))
         loop = 0
    elif choice == 2:
        sub(a=int(input("Subtract this: ")), b=int(input("from this: ")))
        loop = 0
    elif choice == 3:
        mul(a=int(input("Multiply this: ")), b=int(input("by this: ")))
        loop = 0
    elif choice == 4:
        div(a=int(input("Divide this: ")), b=int(input("by this: ")))
        loop = 0
    elif choice == 5:
        loop = 0

print ("Thank you for using calculator.py!")
