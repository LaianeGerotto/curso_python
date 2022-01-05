#Exemplo de FOR e WHILE
'''
for contador in range(1,10): #Usamos quando sabemos o Limite.
    print(contador)
print('Fim')
'''
'''
contador = 1
while contador < 10: # Podemos usar quando sabemos ou não o limite
    print(contador)
    contador += 1
print('Fim')

#Condição de parada
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')