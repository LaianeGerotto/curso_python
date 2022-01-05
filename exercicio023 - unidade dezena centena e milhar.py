n1 = str(input('Digite um número entre 0 a 9999 : '))
n2 = n1.rjust(4,'0')
print('Unidade: ', n2[3])
print('Dezena:  ', n2[2])
print('Centena: ', n2[1])
print('Milhar:  ', n2[0])

#Correção Guanabara
'''n1 = int(input('Digite um número entre 0 a 9999 : '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Unidade: ', u)
print('Dezena:  ', d)
print('Centena: ', c)
print('Milhar:  ', m)'''