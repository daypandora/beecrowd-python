h1 = int(input())
h2 = int(input())

if h2 <= h1:
    h = (24 - h1) + h2
elif h1 < h2:
    h = h2 - h1
print(f'O JOGO DUROU {h} HORA(S)')