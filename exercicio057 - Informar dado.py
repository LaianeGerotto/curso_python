'''
opcao = ''
while opcao != 'F' and opcao != 'M':
        opcao = str(input('Digite o sexo: ')).upper()[0].strip() #[0] é para pegar a primeira letra caso digite Masculino
        if opcao == 'F'or opcao == 'M':
                print('Sexo digitado corretamente!')
        else:
                print('Digite novamente!')
print('Fim!')
'''

#Correção Guanabara

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso')
