#!/usr/bin/env python


numero = int(input('Informe um numero: '))

# init
limit = numero // 2
total = 0

# retirar numero 0 e 1
if numero != 0 and numero != 1:
    total = 1 

if numero % 2 == 0:
    total += limit + 2

for i in range(3, limit):
    if numero % i == 0:
        print(i)
        total +=  numero

if numero == total:
    print('perfeito')
else:
    print('nao perfeito')
