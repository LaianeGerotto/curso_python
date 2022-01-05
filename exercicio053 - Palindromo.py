
frase = str(input('Digite uma frase: ').upper().strip())
palavras = frase.split() #gerou uma lista
fraseJunta = ''.join(palavras) #Juntou tudo numa unica string
fraseInvertida = fraseJunta[::-1] # essa linha substitui o FOR abaixo

'''for letra in range(len(fraseJunta) - 1, -1, -1): #inverteu a frase
    fraseInvertida += fraseJunta[letra]'''
if fraseInvertida == fraseJunta:
    print('A frase digitada É Palíndromo')
else:
    print('A frase digitada Não é Palíndromo')
print(f'Frase normal:    {fraseJunta}')
print(f'Frase invertida: {fraseInvertida}')
