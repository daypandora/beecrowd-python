S = float(input())

if 0 < S <= 400.00:
    r = S * 0.15
    p = '15%'
elif 400.01 <= S <= 800.00:
    r = S * 0.12
    p = '12%'
elif 800.01 <= S <= 1200.00:
    r = S * 0.10
    p = '10%'
elif 1200.01 <= S <= 2000.00:
    r = S * 0.07
    p = '7%'
elif S > 2000.00:
    r = S * 0.04
    p = '4%'
    
print(f'''Novo salario: {S + r:.2f}
Reajuste ganho: {r:.2f}
Em percentual: {p}''')