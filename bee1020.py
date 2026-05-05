D = int(input())
print(f'{D//365} ano(s)')
D %= 365
print(f'{D//30} mes(es)')
D %= 30
print(f'{D} dia(s)')