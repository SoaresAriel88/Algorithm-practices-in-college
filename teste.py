mes = int(input("Digite o mês (1 a 12): "))

while mes < 1 or mes > 12:
    print("Valor inválido!")
    mes = int(input("Digite o mês (1 a 12): "))

print(f"Mês aceito: {mes}")