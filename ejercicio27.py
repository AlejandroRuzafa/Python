frase = input('frase ')
frase_invertida = []
a = 0

for i in range(0,len(frase)):
    frase_invertida.append(frase[ -1 - a ])
    a = a - 1 

print(''.join(frase_invertida))

