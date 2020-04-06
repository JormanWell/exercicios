# Multibanco
# notas disponíveis 100€, 50£, 5€

levantamento = int(input("Quantia a levantar (múltiplos de 5):" ))

# levantamento mínimo

if levantamento < 5:
    print("O levantamento mínimo são 5€")

if levantamento % 5 != 0:
    print("O levantamento só é possível com multiplos de 5€")

# levatamentos até 45€

if levantamento < 50:
    notas5 = levantamento // 5
    print("Levantou", levantamento, "€ em", notas5, "notas de 5€")
elif levantamento < 100:
    notas50 = levantamento // 50  #notas de 50
    sobras = levantamento - notas50 * 50    #rsstante
    notas5 = sobras // 5   # numero de notas de 5 a receber
    print("Levantou", levantamento, "€ em", notas50, "nota de 50€ e", sobras,"€ em", notas5, "notas de 5€")
else:
    levantamento >= 100
    notas100 = levantamento // 100 #notas de 100
    sobras = levantamento - notas100 * 100 #restante
    notas50 = sobras // 50 #notas 50
    sobras5 = sobras - notas50 * 50 #nº de npotas de 50 a receber
    print("Levantou", levantamento, "€ em", notas100, "nota de 100€,", sobras, "€ em", notas50, "notas de 50€," , "e", sobras5, "€ em notas de 5.")
    
    
