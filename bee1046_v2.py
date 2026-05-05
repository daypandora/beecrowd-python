h1, h2 = map(int, input().split())

if h2 <= h1:
   print(f'O JOGO DUROU {(24-h1)+h2} HORA(S)')
elif h1 < h2:
   print(f'O JOGO DUROU {h2 - h1} HORA(S)')