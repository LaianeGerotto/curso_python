pessoa = dict()
lista = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    lista.append(pessoa.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper().strip()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print(lista)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = soma / len(lista)
print(f'B) A média da idade é {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'{p["nome"].upper()} ', end='')
print()
print(f'D) Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print()
print('<< ENCERRADO >>')