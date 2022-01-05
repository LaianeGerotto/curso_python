print('*'*90)
print('{:^90}'.format('LISTA DE TIMES DO BRASILEIRÃO'))
print('*'*90)
print('')
lista = ('CORINTHIANS','PALMEIRAS','SANTOS','GRÊMIO',
        'CRUZEIRO','FLAMENGO','VASCO','CHAPECOENSE',\
        'ATLÉTICO-MG','BOTAFOGO','ATHLETICO','BAHIA',\
        'SÃO PAULO','FLUMINENSE','SPORT','VITÓRIA',\
        'CORITIBA','AVAÍ','PONTE PRETA','ATLÉTICO-GO',)

print(f'Os 5 primeiros são: {lista[0:5]} ')
print()
print(f'Os 4 últimos são: {lista[16:20]}') #OU {lista[-4]}
print()
print(f'Times em ordem alfabética: {sorted(lista)}')
print()
chapecoense = lista.index('CHAPECOENSE') + 1
print(f'O Chapecoense está na {chapecoense}ª posição')
#print(f'O Chapecoense está na {lista.index("CHAPECOENSE")+1}ª posição')

#COrreção Guanabara está igual só usou o item abaixo:
#print(f'O Chapecoense está na {lista.index("CHAPECOENSE")+1}ª posição')