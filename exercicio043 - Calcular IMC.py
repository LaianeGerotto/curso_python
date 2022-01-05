print('Vamos calcular seu IMC?!')
altura = float(input('- Digite sua ALTURA (m): '))
peso = float(input('- Digite seu PESO (kg): '))
imc = peso / (altura * altura)
print('--'*20)
print(f'Seu IMC corresponde a {imc:.2f}')
if imc < 18.5:
    print('- Abaixo do peso.')
elif imc >= 18.5 and imc <= 25: #Guanabara 18.5 <= imc < 25
    print('- Peso ideal.')
elif imc > 25 and imc <= 30: #Guanabara 25 <= imc < 30
    print('- Sobrepeso')
elif imc > 30 and imc <= 40: #Guanabara 30 <= imc < 40
    print('- Obesidade.')
else: #Guanabara imc >= 40
    print('- Obesidade Mórbida.')
