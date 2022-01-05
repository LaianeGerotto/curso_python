nome = str(input('Digite a Cidade: ').upper())
print('A Cidade digitada inicia ou não com SANTO: {} '.format('SANTO' in nome[:5]))

#Correção Guanabara
nome = str(input('Digite a Cidade: ').strip())
print(nome[:5].upper()== 'SANTO')
