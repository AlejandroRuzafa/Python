n1 = int(input('numero 1 '))
n2 = int(input('numero 2 '))
n3 = int(input('numero 3 '))
n4 = int(input('numero 4 '))
n5 = int(input('numero 5 '))
n6 = int(input('numero 6 '))

lista =[n1,n2,n3,n4,n5,n6]
positivos = []
negativos = []


def positivo(n):
    if n > 0:
        return True
    else:
        return False


def media(n): 

    longitud_lista = len(n)
    suma_lista = sum(n)
    media = suma_lista / longitud_lista
    return media

numero_actual = 0

for i in range(1,len(lista)): 
    if positivo(lista[numero_actual]): 
        positivos.append(lista[numero_actual])
    else:
        negativos.append(lista[numero_actual])
    numero_actual = numero_actual + 1 
        
print(media(positivos))
print(sum(negativos))
