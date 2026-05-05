N = int(input())
H = N //3600
N %= 3600
M = N //60
N %= 60
print(f'{H}:{M}:{N}')