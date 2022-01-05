nome = str(input('Qual é seu nome? '))
if nome == 'Amora':
    print('Que nome bonito')
elif nome == 'Chokito' or nome=='Olaff' or nome == 'Meg':
    print('Seu nome não é Popular no Brasil')
elif nome in 'Laiane Meg':
    print('Belo nome!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')