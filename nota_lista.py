tamanho = int(input("Qual tamanho da lista: "))
notas = [] 

for i in range(0, tamanho):
    grade = float(input(f"Digite sua {i + 1} nota: "))
    notas.append(grade)

print(notas)    