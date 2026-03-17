# Criar uma função que terone se o número é Par ou Ímpar 

def par_impar(numero):
    numero_par = numero % 2

    if numero_par == 0:
        return f'O Numero é par'
    return 'Número é impar'

resultado = par_impar(10)
print(resultado, numero)