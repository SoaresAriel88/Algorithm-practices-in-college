soma = 0
contador = 0

while True:
    idade = int(input("Digite uma idade (0 para encerrar): "))

    if idade == 0:
        break

    if idade > 0:
        soma += idade
        contador += 1

# cálculo da média
if contador > 0:
    media = soma / contador
else:
    media = 0

print("Quantidade de idades válidas:", contador)
print("Soma das idades:", soma)
print("Média das idades: {:.2f}".format(media))