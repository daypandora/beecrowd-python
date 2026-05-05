n = int(input())

for i in range(n):
    impar = 0

    x, y = map(int, input().split())
  
    if x > y:
      x, y = y, x

    for j in range(x+1, y):
        if j % 2 != 0:
            impar += j
    print(impar)