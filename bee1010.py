cod1, qtd1, valor1 = input().split()
cod1, qtd1, valor1 = int(cod1), int(qtd1), float(valor1)

cod2, qtd2, valor2 = input().split()
cod2, qtd2, valor2 = int(cod2), int(qtd2), float(valor2)

print(f'VALOR A PAGAR: R$ {(qtd1*valor1) + (qtd2*valor2):.2f}')