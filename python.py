# EX1

# def sep_eq(cod, stt):
#     pend = []
#     concl = []
#     for i in range(len(cod)):
#         if stt[i] == 0:
#             pend.append(cod[i])
#         else:
#             concl.append(cod[i])
#     return pend, concl

# cod_eq = [101, 102, 103, 104, 105, 106, 107, 108]
# stt_manutencao = [0, 1, 0, 1, 0, 1, 1, 0]

# print(f"Equipamentos Pendentes: {sep_eq(cod_eq,stt_manutencao)[0]}")
# print(f"Equipamentos Concluidos: {sep_eq(cod_eq,stt_manutencao)[1]}")


###################################################################################################################################



# EX2
# def class_prod():
#     prod_aprov = []
#     prod_reprov = []
#     prod_pend = []
    
#     for i in range(10):
#         num_serie = input(f"Digite o número de série do produto {i+1}: ")
#         while True:
#             try:
#                 status = int(input(f"Digite o status de qualidade do produto {num_serie} (1 = aprovado, 0 = reprovado, -1 = pendente): "))
#                 if status in [1, 0, -1]:
#                     break
#                 else:
#                     print("Entrada inválida! Digite apenas 1, 0 ou -1.")
#             except ValueError:
#                 print("Entrada inválida! Digite um número inteiro.")

#         if status == 1:
#             prod_aprov.append(num_serie)
#         elif status == 0:
#             prod_reprov.append(num_serie)
#         else:
#             prod_pend.append(num_serie)

#     return prod_aprov, prod_reprov, prod_pend


# aprovados, reprovados, pendentes = class_prod()

# print("\nResumo da Classificação dos Produtos:")
# print(f"Produtos Aprovados: {aprovados}")
# print(f"Produtos Reprovados: {reprovados}")
# print(f"Produtos Pendentes: {pendentes}")