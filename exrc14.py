# Objetivo é criar uma função que multiplique todos os argumentos nao nomeados e retorne o valor em uma variável 

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplicar(2, 3, 7, 8, 34)
print(resultado)

