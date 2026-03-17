# Criar uma função que terone se o número é Par ou Ímpar 

def par_impar(numero):
    numero_par = numero % 2 == 0

    if numero_par:
        return f'O Numero {numero} é par'
    return f'Número {numero} é impar'

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)

print(dois_e_par)
print(par_impar(3))