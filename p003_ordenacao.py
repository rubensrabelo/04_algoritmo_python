def buscaMenor(arr):
    menor = arr[0]
    menor_indice = 0
    for i in range(1, len(arr)):
        if menor < arr[i]:
            menor = arr[i]
            menor_indice = i
    return menor_indice


def ordenacaoPorSelecao(arr):
    novoArr = list()
    for i in range(1, len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr

ordenacao = ordenacaoPorSelecao([1,  4, 88, 55, 10, 100])

print(ordenacao)