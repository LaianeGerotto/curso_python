#Tuplas ()
#Listas []
#Dicionário {}

# pessoas = {'nome': 'Meg', 'sexo': 'F', 'idade': '7'}
# print(pessoas)
# print(pessoas['nome'])
# print(pessoas.items())
# print(pessoas.values())
# print(pessoas.keys())
# del pessoas['sexo'] #para apagar
# pessoas['nome] = 'Juju' #Altera Meg para Juju
# pessoas['peso'] = 15 #para adicionar um novo elemento
# for k in pessoas.items():
#     print(k)

# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil)
# print(brasil[0])
# print(brasil[1]['uf'])

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #em dicionário não funciona [:]
for e in brasil:
    # for k, v in e.items():
    #     print(f'O campo {k} tem o valor {v}.')
    for v in e.values():
        print(v, end='')
    print()