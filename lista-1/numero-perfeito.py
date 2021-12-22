#!/usr/bin/env python
import pdb

def numero_perfeito(numero):

    total = 0
    for i in range(1, numero):
        if numero % i == 0:
            total += i
    
    if total == numero:
        return True
    else:
        return False


for i in range(1, 500):
    if numero_perfeito(i):
        print(i)

