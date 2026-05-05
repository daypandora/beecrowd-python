numero_testes = int(input())

for i in range(numero_testes):
    x, y = map(int, input().split())
    
    if y == 0:
        print('divisao impossivel')
    else:
        print(f'{x/y:.1f}')