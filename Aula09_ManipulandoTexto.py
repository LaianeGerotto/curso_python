frase = 'Curso em Video Python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])
print(frase.count('o')) #conta quantas letras 'o' a frase possui
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Python', 'Android')) #troca a palavra definitivo precisar fazer uma nova atribuição print(frase)
print('Curso' in frase)
print(frase.find('Video'))
print(frase.split())
dividido = frase.split() # dividir a frase em Lista
print(dividido[0]) #numero é a posição da lista
print(dividido[2][3]) #2 é o item da lista(video) 3 é a letra 'e'


'''print("""Um anagrama é uma palavra que é feita a partir da
transposição das letras de outra palavra ou frase. Por exemplo,
“Iracema” é um anagrama para “America”. Escreva um programa
que decida se uma string é um anagrama de outra string,
ignorando os espaços em branco.""")'''