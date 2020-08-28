frase = input('frase ')
letra = input('letra ')
frase_final = []

while len(letra) != 1 :
    print('debe ser solo una letra ')
    letra = input('letra ')

letra_actual = 0 

for i in range(0,len(frase)):
    if frase[letra_actual] == letra :
        frase_final.append('*')
    else: 
        frase_final.append(frase[letra_actual])
    letra_actual = letra_actual + 1 

print(''.join(frase_final))





    