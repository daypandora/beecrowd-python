valores = []

for _ in range(5):
    valores.append(int(input()))

maior = max(valores)
pos = valores.index(maior) + 1

print(maior)
print(pos)