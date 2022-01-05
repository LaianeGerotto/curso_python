frase = str(input('Digite uma frase: ').upper())
print(frase)
print('- A frase possui {} letras A.'.format(frase.count('A')))
primeira = frase.find('A')+1
print('- Sua frase tem a primeira a letra A na posicao',primeira,'.')
ultima = frase.rfind('A')+1
print('- Sua frase tem a ultima a letra A na posicao',ultima,'.')