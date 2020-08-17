def promedio(*n): 

    longitud_lista = len(n)
    suma_lista = 0
    for i in n :
        suma_lista = suma_lista + i 
    media = suma_lista / longitud_lista
    return media

    # return sum(n) / len(n)