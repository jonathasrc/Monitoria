#!/usr/bin/env python

anterior = 0
proximo = 0
while proximo < 10:
    print(proximo)
    proximo = proximo + anterior
    anterior = proximo - anterior

    if proximo == 0:
        proximo +=1
