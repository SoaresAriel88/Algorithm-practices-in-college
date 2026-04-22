classificacao = ""
altura = float(input("Qual é a sua altura "))
peso = float(input("Qual é seu peso "))
if peso < 0 and altura < 0:
    print("Dados inválidos")
else:
    imc = peso / (altura **2)
    if imc > 17.5:
        print("Abaixo do peso")
    elif 20 >= imc >= 17.5:
        print("Peso ideal")
    elif 25 >= imc >= 20:
        print("Sobrepeso")