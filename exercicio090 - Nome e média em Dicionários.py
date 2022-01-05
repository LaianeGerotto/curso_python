'''
boletim = dict()
boletim["nome"] = str(input('Nome: '))
boletim["media"] = float(input((f'Média de {boletim["nome"]}: ')))
if boletim["media"] < 5:
    boletim["situacao"] = 'Reprovado'
elif boletim["media"] >= 5 and boletim["media"] < 7:
    boletim["situacao"] = 'Recuperação'
elif boletim["media"] >= 7 and boletim["media"] <= 10:
    boletim["situacao"] = 'Aprovado'
print('-='*20)
print(f'  - Nome é igual a {boletim["nome"]}')
print(f'  - Média é igual a {boletim["media"]}')
print(f'  - Situação é igual a {boletim["situacao"]}')
'''

#Correção Guanabara
aluno = dict()
aluno["nome"] = str(input('Nome: '))
aluno["media"] = float(input((f'Média de {aluno["nome"]}: ')))
if aluno["media"] >= 7:
    aluno["situacao"] = 'Aprovado'
elif 5 <= aluno["media"] < 7:
    aluno["situacao"] = 'Recuperação'
else:
    aluno["situacao"] = 'Reprovado'
print('-='*20)

for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')