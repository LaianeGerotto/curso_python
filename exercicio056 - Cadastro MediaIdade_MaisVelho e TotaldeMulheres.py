'''
somaidade = 0
mediaidade = 0
hvelho = 0
contadorF = 0
nomeHomem = ''
for contador in range (0,2):
    print(f'DADOS DA {contador+1}º PESSOA')
    nome = input('NOME: ').strip()
    idade = (int(input('IDADE: ')))
    sexo = input('SEXO [F/M]: ').upper().strip()
    somaidade += idade
    print('----------------------------------------------------------------')
    if sexo == 'M':
        if idade > hvelho:
            hvelho = idade
            nomeHomem = nome
    if sexo == 'F':
        if idade < 20:
            contadorF += 1
    mediaidade = somaidade / 4
print(f'A média entre as idades das 4 pessoas é {mediaidade/4} anos')
print(f'O {nomeHomem} é o homem mais velho e tem {hvelho} anos.')
print((f'Nessa relação há {contadorF} mulheres com menos de 20 anos.'))

'''
#Resolução Guanabara
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print(f'----- {p}ª pessoa -----')
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))