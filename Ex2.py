estacionamento = []

carangos = ["Uno", "Gol", "Civic", "Corolla", "Palio", "Onix", "HB20", "Ka", "Fusca", "Jeep"]

print("Ordem de entrada dos carangos:")
for carango in carangos:
    estacionamento.append(carango)
    print(f"Entrou: {carango}")

print("\n Sequência de saída dos carangos (LIFO):")
while estacionamento:
    carango = estacionamento.pop()
    print(f"Saiu: {carango}")
