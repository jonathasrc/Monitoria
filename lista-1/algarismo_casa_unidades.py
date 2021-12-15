#!/usr/bin/env python

numero = int(input('Digite um numero inteiro positivo: '))

if numero < 0:
    numero = numero * -1
    unidade = numero % 10
    print(unidade * -1)
else:
    unidade = numero % 10
    print(unidade)


