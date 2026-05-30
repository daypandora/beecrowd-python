numero_testes = int(input())
count = 1

for i in range(numero_testes*4):
    if count % 4 == 0:
       print("PUM")
    else:
       print(count, end=" ")        
    count += 1