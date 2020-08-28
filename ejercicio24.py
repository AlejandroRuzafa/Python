
def vocal(a):
    if a == 'i' or a =='a' or a =='e' or a =='o' or a =='u'  :
        return True
    else:
        return False


def n_vocales_texto(texto):
    n = 0
    letra_actual= 0 
    for letra_actual in range(0,len(texto)):
        if vocal(texto[letra_actual]):
            n = n + 1 
        letra_actual = letra_actual + 1
    print(f'en el texto hay {n} vocales ')






