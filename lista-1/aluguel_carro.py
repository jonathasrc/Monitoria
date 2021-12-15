#!/usr/bin/env python
#TODO: fazer passar em todos testes no thehuxley
diaria = 30
locacao = 0.01

dias = int(input())
kilometros = int(input())
resultado = (diaria * dias) + (kilometros * locacao)
print(round(resultado * 0.9, 2))
