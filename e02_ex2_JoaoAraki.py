notas = []
notasAcimaDaMedia = 0

for i in range(6):
    notas.append(int(input(f"Adicione a nota {i + 1} de 0 a 10 ")))

print("Maior:", max(notas))
print("Menor:", min(notas))
print("Media:", sum(notas) / len(notas))

for x in range(len(notas)):
    if notas[x] >= 6:
       notasAcimaDaMedia += 1
    

print("Notas acima da média:", notasAcimaDaMedia)