# Criar uma função que terone se o número é Par ou Ímpar 

def par_impar(numero):
    numero_par = numero % 2 == 0

    if numero_par == 0:
        return f'O Numero {numero} é par'
    return f'Número {numero} é impar'

resultado = par_impar
print(resultado(3))