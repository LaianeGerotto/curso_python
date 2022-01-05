# from datetime import date
# cadastro = dict()
# cadastro['nome'] = str(input('Nome: '))
# cadastro['idade'] = int(input('Ano de Nascimento: '))
# cadastro['idade'] = date.today().year - cadastro['idade']
# cadastro['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
# if cadastro['ctps'] != 0:
#     cadastro['contratação'] = int(input('Ano de Contratação: '))
#     cadastro['salario'] = float(input('Salário: R$ '))
#     cadastro['aposentadoria'] = date.today().year - cadastro['contratação']
#     cadastro['aposentadoria'] = 35 - cadastro['aposentadoria'] + cadastro['idade']
# print('*'*40)
#
# for k, v in cadastro.items():
#     print(f'  - {k} tem o valor {v}')

#Correção Guanabara
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-='*30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')

