'''
maior18 = homens = mulheres20 = 0

while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    idade = int(input('Idade: '))
    while idade < 1 and idade > 120:
        idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()
    print('=-'*15)
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulheres20 += 1
    opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    while opcao not in 'SN':
        opcao = str(input('Deseja continuar? [S/N] ')).upper().strip()
    print('=-' * 15)
    if opcao == 'N':
        break
print(f'Foram cadastrados {maior18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {homens} Homens.')
print(f'Foram cadastradas {mulheres20} Mulheres com menos de 20 anos.')'''

#Correção Guanabara
tot18 = totH = totM20 = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastrados {tot18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {totH} Homens.')
print(f'Foram cadastradas {totM20} Mulheres com menos de 20 anos.')