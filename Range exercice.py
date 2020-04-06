# [1, 2, 3] --> 6
count = 0
for number in range(1, 4):
    count = count + number   # nova contagem + a velha contagem
    
print(count)

# outro modo de fazer
def sum_list(my_list):
    count = 0
    for number in my_list:
        count = count + number
        print(my_list)

print(count)
