x = int(input())
y = int(input())

soma = 0 

if x > y:
   x, y = y, x #troca os valores de x e y, para que x seja sempre o maior
   
for i in range(x, y+1):
    if i % 13 != 0:
        soma += i
print(soma)