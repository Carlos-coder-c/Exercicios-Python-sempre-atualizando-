# Fazeer um projeto simples para logica
email_google = str(input('Digite seu email: '))

def google(email: dict[str, str]) -> str:
  match email:
    case {"type": "user", "email": email_user} if email_user.endswith('@gmail.com'):
       create_conta(email_user) # type: ignore
       return 'Conta criada com  todo sucesso do mundo!'
     
    case {"type": "user", "email": _}:
      return 'Só aceitamos emails Google'
    
    case _:
      'Invalido'
      
google(email_google)
