a = [45, 12, 1, -4, 63, 0, -7, 12, 2]
  
longitud = len(a)

solucion = []

for i in range( 0 , longitud ):
    if a[i] < 5:
        solucion.append(a[i])

print(solucion)

