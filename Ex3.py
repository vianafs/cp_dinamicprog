
def ordenar_lista():
    lista = [7, 3, 11, 5, 8, 15, 14]
    print("Lista original:", lista)

    
    lista.sort()
    print("Lista ordenada:", lista)



def atender_clientes():
    fila = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4", "Cliente 5"]
    
    print("Clientes na fila:")
    for cliente in fila:
        print(cliente)

    print("\nAtendendo os clientes:")
    while fila:
        cliente_atendido = fila.pop(0)
        print("Atendido:", cliente_atendido)



def retirar_carros():
    estacionamento = ["Uno", "Gol", "Civic", "Corolla", "Palio", "Onix", "HB20", "Ka", "Fusca", "Jeep"]

    print("Carros que entraram no estacionamento:")
    for carro in estacionamento:
        print(carro)

    print("\nRetirando os carros:")
    while estacionamento:
        carro_saiu = estacionamento.pop()
        print("Saiu:", carro_saiu)



def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Ordenar a lista (Exercício 1)")
        print("2 - Atender clientes (Exercício 2 - FIFO)")
        print("3 - Retirar carros (Exercício 3 - LIFO)")
        print("4 - Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            ordenar_lista()
        elif opcao == "2":
            atender_clientes()
        elif opcao == "3":
            retirar_carros()
        elif opcao == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
