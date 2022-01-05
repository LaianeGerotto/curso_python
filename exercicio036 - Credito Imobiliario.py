print('*'*21)
print(' Crédito Imobiliário')
print('*'*21)
print('Preencha as informações abaixo:')
casa = float(input('- Qual valor do Imóvel? R$ '))
salario = float(input('- Qual é o seu salário? R$ '))
periodo = int(input('- Em quantos anos deseja financiar? '))
meses = periodo*12
parcela = casa/meses
if parcela >= (0.3 * salario):
    print('No cenário atual, não é possível liberar o Crédito!')
elif parcela < (0.3 * salario):
    print(f'Crédito pré aprovado, parcela mensal de R${parcela:.2f} por {meses} meses.')


