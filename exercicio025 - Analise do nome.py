nome = str(input('Digite o nome completo: ').upper())
print('O nome digitado tem ou não a palavra Silva: {} '.format('SILVA' in nome[::]))

#Correção Guanabara
nome = str(input('Digite o nome completo: ').strip())
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))