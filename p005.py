from random import choice

with open('listaFrutas.txt', 'a') as arquivo:
    arquivo.write('Banana\n')
    arquivo.write('Maçã\n')
    arquivo.write('Acerola\n')
    arquivo.write('Pera\n')

with open('listaFrutas.txt', 'r') as arquivo:
    listaFrutas = list()

    for linha in arquivo:
        fruta = linha.strip()
        listaFrutas.append(fruta)

valor = choice(listaFrutas)

print(f'O valor escolhido foi {valor}.')