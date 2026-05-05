validas = 0
soma = 0
while True:
    nota = float(input())

    if 0 <= nota <= 10:
       validas += 1
       soma += nota
    else:
       print('nota invalida')

    if validas == 2: 
       break
print(f'media = {soma/2:.2f}')