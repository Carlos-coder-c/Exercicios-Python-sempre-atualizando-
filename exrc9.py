seu_nome = str(input("Digite seu primeiro nome: "))

resultado = len(seu_nome)

if resultado <= 4:
     print(f'Seu nome {seu_nome}, ele tem {resultado} letras ')
     print("Ele é curto")

if resultado  == 5 or 6:
    print(f"Seu nome {seu_nome}, contem {resultado} letras")
    print("Seu nome é normal")

 elif resultado > 6:
     print("Seu nome é grande")

