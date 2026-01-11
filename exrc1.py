# Calculadora do IMC Calculo usado = divide seu peso (em kg) pela sua altura (em metros) ao quadrado (altura x altura), usando a fórmula IMC = peso / (altura)²

peso = float(input('Qual seu peso:  '))
altura = float(input('Qual sua altura:  '))
IMC = peso / (altura * altura)
print(f' Seu Imc é de {IMC:.5f}')

if IMC <= 24.9:
  print('Seu nivel de IMC está Normal, Resultado: Normal')
  
  print('Seu nivel de IMC é de Sobrepeso')


elif IMC >= 30.0 and IMC <=  34.9:
    print('Seu nivel de IMC é de Obesidade Grau I')
    
elif IMC >= 35.0 and IMC <= 39.9:
    print('Seu nivel de IMC é de Obesidade Grau II')

elif IMC <= 40.0:
    print('Seu nivel de IMC é de Obesidade Grau III')
    
print('Fim do programa')


