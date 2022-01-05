nome = str(input('Digite seu nome Completo: ').strip())
dividido = nome.split()
#semespaco = "".join(nome.split())
print('1- Nome digitado pelo usuário: {} '.format(nome))
print('2- O nome com todas as letras maiúsculas: {} '.format(nome.upper()))
print('3- O nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('4- Quantas letras ao todo (sem espaços): {}'.format(len(nome) - nome.count(' ')))
print('5- Quantas letras tem o primero nome: {}' .format(len(dividido[0]))) #versão Guanabara .format(nome.find(' '))

