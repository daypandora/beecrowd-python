positivos = 0
soma = 0
for i in range(6):
    x = float(input())
    
    if x > 0:
        soma += x
        positivos +=1
        
media = soma/positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')