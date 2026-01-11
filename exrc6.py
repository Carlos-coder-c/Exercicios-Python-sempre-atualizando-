nome_usuario = str(input('Qual seu nome Completo: '))
idade_usuario = int(input('Qual sua idade: '))

nome_invertido = nome_usuario[::-1]

quantidade_letras = len(nome_usuario)

qtd_espacos = nome_usuario.count(' ')

if nome_usuario and idade_usuario:
  print(f'Seu nome é: {nome_usuario}, e voce tem {idade_usuario} anos')
  print(f'Seu nome invertido é: {nome_invertido}')

  if qtd_espacos > 0:
   print(f'O seu nome contem {qtd_espacos} espaços')
  else:
   print('Seu nome nao contem espaços')

  print(f'Seu nome tem {quantidade_letras} letras')
  
  print(f'A primeira letra de seu nome é {nome_usuario[0]}')

  print(f'A ultima letra de seu nome é {nome_usuario[-1]}')

else:
    print('Campo VAZIO')