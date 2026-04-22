qtd_Grande = 0
qtd_compras = 0
qtd_Media = 0
qtd_Pequena = 0
somaCompras = 0
mediaCompras = 0

while True:
    compras = float(input("Digite o valor da sua compra, se quiser cancelar digite (0): "))
    if compras == 0:
        break
    
    if compras < 0:
        print("Valor negativo ignorado")
        continue
    
    else:
        qtd_compras += 1
        if compras < 50:
            faixa = "Pequena"
            qtd_Pequena += 1
            somaCompras += compras
        elif compras < 200:
            faixa = "Média"
            qtd_Media += 1
            somaCompras += compras
        elif compras >= 200:
            faixa = "Grande"
            qtd_Grande += 1
            somaCompras += compras


print(f"Total de compras válidas: {qtd_compras}, Soma total: R${somaCompras}")

if qtd_compras > 0:
    media = somaCompras / qtd_compras
    print(f"Média: R$ {media:.2f}")
else:
    print("Média: R$ 0.00")


print(f"Quantidade Faixa Pequena {qtd_Pequena}")
print(f"Quantidade Faixa Media {qtd_Media}")
print(f"Quantidade Faixa Grande {qtd_Grande}")
