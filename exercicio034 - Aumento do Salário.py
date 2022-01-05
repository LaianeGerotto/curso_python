salario = float(input('Digite seu salário: R$ '))
if salario > 1250:
    aumento = salario * 0.10
    novosalario = salario + aumento
else:
    aumento = salario * 0.15
    novosalario = salario + aumento
print(f'Seu novo salário é R${novosalario:.2f}')
