#!/usr/bin/env python
''''''
#TODO:DEIXAR COMPATIVEL COM AS ENTRADAS E SAIDAS DO THEHUXLEY
lista_compra = []

def INSERIR(lista_compra, produto):
    lista_compra.append(produto)

def PROCURAR_NOME(lista_compra, nome):
    for produto in lista_compra:
        if produto['nome'] == nome:
            return produto

def CONSULTAR(lista_compra):
    soma = 0
    for produto in lista_compra:
        soma += produto['valor'] * produto['quantidade']
    return f'Atualmente a lista esta R${soma}'

def REMOVER_NOME(lista_compra, nome, quantidade):
    index = 0
    for produto in lista_compra:
        if produto['nome'] == nome:
            if produto['quantidade'] <= quantidade:
                lista_compra.pop(index)
            else:
                lista_compra[index]['quantidade'] -= quantidade
        index += 1

def REMOVER_GRUPO(lista_compra, valor):
    index = 0

    for produto in lista_compra:
        total = produto['quantidade'] * produto['valor']
        if total >= valor:
            lista_compra.pop(index)

        index += 1


computador = {'nome':'computador','valor':3, 'quantidade': 5}
mouse = {'nome':'mouse','valor':100, 'quantidade': 5}
INSERIR(lista_compra, computador)
INSERIR(lista_compra, mouse)
print(PROCURAR_NOME(lista_compra, 'mouse'))
print(REMOVER_NOME(lista_compra, 'mouse', 3))
print(CONSULTAR(lista_compra))
REMOVER_GRUPO(lista_compra, 100)
print(lista_compra)

