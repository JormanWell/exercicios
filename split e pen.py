#SPLIT  .split

'maça-45-massa-arroz'.split('-')    # elimina o caractere e devolve como lista
# ['maça', '45', 'massa', 'arroz']

dados = '012A45A789'
dados.split('A')
# ['012', '45', '789']

# selecionar elementos da lista

primeiros = dados.split('A')[0]
primeiros
# '012'
segundos = dados.split('A')[1]
segundos
# '45'

primeiros, segundos, terceiros = dados.split('A')
primeiros
# '012'
segundos
# '45'
terceiros
# '789'

# APPEND  .append

lista = ['maça', 45, 'massa', 'arroz']  # coloca mais um elemento na lista
lista.append('açucar')                  # ( só um de cda vez)
# ['maça', 45, 'massa', 'arroz', 'açucar']
