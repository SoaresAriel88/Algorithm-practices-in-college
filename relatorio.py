# leitura e validação de n
n = int(input("Digite a quantidade de vendedores: "))
while n <= 0:
    print("Valor inválido! Digite um número maior que 0.")
    n = int(input("Digite a quantidade de vendedores: "))

i = 0
soma_vendas = 0

qtd_destaque = 0
qtd_regular = 0
qtd_baixo = 0

# loop principal
while i < n:
    venda = float(input(f"Digite a venda do vendedor {i+1}: "))
    soma_vendas += venda
    if venda < 0:
        media_vendas = 0
        soma_vendas = 0
        break
    
    else:
        if venda >= 5000:
            classificacao = "Destaque"
            qtd_destaque += 1
        elif venda >= 2000:
            classificacao = "Regular"
            qtd_regular += 1
        else:
            classificacao = "Baixo desempenho"
            qtd_baixo += 1

        print(f"Vendedor {i+1}: venda={venda:.2f} - {classificacao}")

        i += 1

# cálculos finais
media_vendas = soma_vendas / n
percentual_destaque = (qtd_destaque / n) * 100

# saída final
print("\nResumo:")
print(f"Quantidade em destaque: {qtd_destaque}")
print(f"Quantidade em regular: {qtd_regular}")
print(f"Quantidade em baixo desempenho: {qtd_baixo}")
print(f"Média de vendas: {media_vendas:.2f}")
print(f"Percentual de destaque: {percentual_destaque:.1f}%")