with open('arq.txt', 'r') as arquivo:
    documento = arquivo.readlines()

for frase in documento:
    print(frase)