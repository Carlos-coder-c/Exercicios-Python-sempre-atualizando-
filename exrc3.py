'''''
Execicio de Or e and 3 desafios
1- lOGICA de and
2 - Logica de or
3 desafio final junção dos 2
'''''
print('---Seja--bem--vindo--ao--seu--Banco---')
print('''Digite uma das  opções
    E para entrar ou S para sair''')

escolha1 = input('Digite sua escolha: ')
senha_verificada = input('Digite sua senha: ')
senha = 'c0907138H'
while True:
 if escolha1 == 'E' or 'e' and senha_verificada == senha:
  print('Acesso Permitido!')

  
 elif escolha1 == 'S' or 's' and sair == 'Sim ' or 'sim'  : # type: ignore
  print('Você deseja sair mesmo?')
  sair = input('Confirma?? Digite Sim')
  
 else:
    print('Acesso negado!')
 break
