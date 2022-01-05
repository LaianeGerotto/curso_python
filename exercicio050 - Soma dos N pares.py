s = 0
contador2 = 0
for contador in range(0,6):
    n = int(input(f'Digite {contador +1}º número: '))
    if n % 2 == 0:
        s +=n
        contador2 += 1
print(f'Você informou {contador2} números Pares e a SOMA dos números pares digitados é {s}.')