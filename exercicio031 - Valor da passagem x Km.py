n1 = float(input('Digite a distância da sua viagem em KM: '))
if n1 <=200:
    passagem = n1 * 0.50
    print(f'O valor da sua passagem é R${passagem:.2f}')
else:
    passagem = n1 * 0.45
    print(f'O valor da sua passagem é R${passagem:.2f} ')
