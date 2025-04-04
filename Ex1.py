# Dada a lista ordenada [3, 5, 7, 8, 11, 14, 15], 
# utilize o algoritmo de busca binária para encontrar o valor 11.
# Retorne o índice do alvo e mostre o funcionamento do algoritmo passo a passo (a cada iteração).

def busca(lista, alvo):
    start = 0
    end = len(lista) - 1
    iteracao = 1

    while start <= end:
        mid = (start + end) // 2
        print(f"Iteração {iteracao}:")
        print(f"Início = {start}, Fim = {end}, meio = {mid}")
        print(f"Valor no meio = {lista[mid]}\n")

        if lista[mid] == alvo:
            print(f"Valor {alvo} encontrado no índice {mid}.")
            return mid
        elif lista[mid] < alvo:
            start = mid + 1
        else:
            end = mid - 1

        iteracao += 1

    print(f"Valor {alvo} não encontrado na lista.")
    return -1

lista = [3, 5, 7, 8, 11, 14, 15]
alvo = 11
busca(lista, alvo)
