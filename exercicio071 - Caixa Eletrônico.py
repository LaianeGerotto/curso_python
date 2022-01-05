'''
print('=='*10)
print('    BANCO DOG') #print('{:^30}'.format('BANCO DOG'))
print('=='*10)
valor = int(input('Qual valor você deseja sacar? R$'))
total = resto = 0
valor50 = int(valor/50)
resto = int(valor % 50)

valor20 = int(resto / 20)
resto = int(resto % 20)

valor10 = int(resto / 10)
resto = int(resto % 10)

valor01 = int(resto / 1)
resto = int(resto % 1)

if valor50 > 0:
    print(f'Total de {valor50} cédulas de R$50')
if valor20 > 0:
    print(f'Total de {valor20} cédulas de R$20')
if valor10 > 0:
    print(f'Total de {valor10} cédulas de R$10')
if valor01 > 0:
    print(f'Total de {valor01} cédulas de R$1')
print('***************************')
print('     Volte sempre!!!')
print('       Banco DOG')'''

#Correção Guanabara
print('='*30)
print('{:^30}'.format('BANCO DOG'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Volte sempre ao BANCO DOG! Tenha um bom dia!')
