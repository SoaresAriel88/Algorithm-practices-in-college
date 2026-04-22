# Check if the variable 'nota' has the highest value; if not, break the while true loop.   
while True:
    nota = float(input("Digite uma nota: "))

    if nota <= 10 and nota >= 0:
        break
    else:
        print("A nota só pode ser de 0 a 10, digite novamente: ")

# Condition at nota variable
if nota >= 9:
    print("Excelente")
    print(f"Nota: {nota:.2f}")
elif nota >= 7:
    print("Bom")
    print(f"Nota: {nota:.2f}")
elif nota >= 5:
    print("Regular")
    print(f"Nota: {nota:.2f}")
else:
    print("Insuficiente")
    print(f"Nota: {nota:.2f}")