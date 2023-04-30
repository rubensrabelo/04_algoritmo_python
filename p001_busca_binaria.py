#BUSCA BINÁRIA

def buscaBinaria(lista, item): #item = valor procurado pelo o usuário
    baixo = 0 # ambos representam os índices da minha lista
    alto = len(lista) - 1

    while baixo <= alto:
        meio = int((baixo + alto)/2)
        chute = lista[meio]

        if chute == item:
            return meio
        elif chute > item:
            alto = meio - 1
        elif chute < item:
            baixo = meio + 1
        else:
            return None

minhaLista = [1, 3, 5, 7, 9, 10, 11]

print(buscaBinaria(minhaLista, 10))
print(buscaBinaria(minhaLista, -1))