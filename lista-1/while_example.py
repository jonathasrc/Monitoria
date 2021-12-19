#!/usr/bin/env python
contador = 0
soma = 0


# while contador <= 500: #True
#     contador += 1

#      # 0 = 0 + 1
#      # 1 = 1 = 1
#      # 2 = 2 + 1 ....

    
#     if contador % 2 == 0:
#         soma = soma + contador 
#         # 0 = 0 + 2
#         # 2 = 2 + 4
#         # 6 = 4 + 6

for i in range(0, 501,2):
    soma += i


print(soma)
