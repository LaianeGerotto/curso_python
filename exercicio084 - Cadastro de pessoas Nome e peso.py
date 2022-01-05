cadastro = list()
dado = list()
maiorPeso = menorPeso = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(cadastro) == 0:
        maiorPeso = menorPeso = dado[1]
    else:
        if dado[1] > maiorPeso:
            maiorPeso = dado[1]
        if dado[1] < menorPeso:
            menorPeso = dado[1]
    cadastro.append(dado[:])
    dado.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper()
    if resp == 'N':
        break

print(f'Ao todo, você cadastrou {len(cadastro)} pessoas')
print(f'O maior peso foi de {maiorPeso}kg. O peso de ', end='')
for pessoa in cadastro:
      if pessoa[1] == maiorPeso:
            print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O menor peso foi de {menorPeso}kg. O peso de ', end='')
for pessoa in cadastro:
      if pessoa[1] == menorPeso:
          print(f'[{pessoa[0]}]')



