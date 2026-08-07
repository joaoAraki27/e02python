matriz = []
somaTotal = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"valor [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

print(matriz)

for i in range(3):
        print(f"linha {i+1}:", sum(matriz[i]))
        somaTotal += sum(matriz[i])

print("Soma total da matriz:", somaTotal)

#DESAFIOS
#somar colunas 
for i in range(3):
    somaColuna = 0
    for j in range(3):
        somaColuna += matriz[j][i]
    print(f"Coluna {i}: {somaColuna}")

#maior valor da matriz
maior = 0
linhaMaior = 0
colunaMaior = 0

for i in range(3):
    for j in range(3):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            linhaMaior = i
            colunaMaior = j

print(f"Maior valor: {maior}")
print(f"Está na linha {linhaMaior} e coluna {colunaMaior}")