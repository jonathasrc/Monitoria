#!/usr/bin/python


media = float(input())
aulas = int(input())
faltas = int(input())
frequencia = ((aulas - faltas)/aulas) * 100

if frequencia >= 75 and media >= 5:
    print('APROVADO')
elif frequencia >= 50 and media >= 7:
    print('APROVADO')
else:
    print('REPROVADO')

