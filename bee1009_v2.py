nome = input()
a = float(input())
b = float(input())

def bonus(a, b):
    return a + (b * 0.15)
    
salario = bonus(a, b)

print(f'TOTAL = R$ {salario:.2f}')