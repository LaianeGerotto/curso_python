# Faça um programa que leia algo e informe o tipo
a = input('Digite algo: ')
print('- O tipo primitivo digitado é ', type(a))
print('- Só tem espaços?', a.isspace())
print('- É um número?', a.isnumeric())
print('_ É alfabético?', a.isalpha())
print('- É alfanúmerico?', a.isalnum())
print('- Está em maiúsculas?', a.isupper())
print('- Está em minúsculas?', a.islower())
print('- Está capitalizada?', a.istitle())


