string = input('word')
num = int(input('num'))

for i in string:
    new_str = string[num:]
    
print(new_str)

#------------------------
def removeChars(str, n):
  return str[n:]

print("Removing n number of chars")
print(removeChars("pynative", 4))