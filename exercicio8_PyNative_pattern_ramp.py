#num = int(input("number:"))

def pattern_ramp(num):
    count = 0
    for i in list(range(num +1 )[1:]):
        degrau = count + i
        if i == i:
            print(str(degrau) * i, end=' ' "\n")
        
pattern_ramp(5)
                  
                  
for num in range(10):
    for i in range(num):
        print (num, end=" ") #print number
    # new line after each row to display pattern correctly
    print("\n")
    
    
print("Second Number Pattern ")
lastNumber = 6
for row in range(1, lastNumber):
    for column in range(1, row + 1):
        print(column, end=' ')
    print("")
    
print('Second number pattern inverted')

n = 5
k = 5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print("\n")