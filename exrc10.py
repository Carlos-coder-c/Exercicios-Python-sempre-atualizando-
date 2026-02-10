# Declarando Variáveis 

numero = int(input('Digite um número inteiro: '))

num_par = numero / 2 
num_impar = numero  % 2 != 0

if numero == num_par:
     print(f'O número {numero}, ele é par!')
 
 
if numero == num_impar:
     print(f"O numero {numero}, é impar")

else:
     print("Você nao digitou número inteiros ")
  