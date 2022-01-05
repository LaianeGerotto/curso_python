import math
print('Teorema de Pitágoras')
n1 = int(input('Cateto adjacente (maior): '))
n2 = int(input('Cateto oposto (menor): '))
hip = math.pow(n1, 2) + math.pow(n2,2) #hip=math.hypot(n1,n2)
print('O comprimento da Hipotenusa de um triangulo retângulo é {}'.format(math.sqrt(hip)))