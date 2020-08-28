
n = int(input('numero '))
a = 0
numero_actual = a
divisores = []

for i in range(1,n+1):
    numero_actual = numero_actual + 1 
    if n % numero_actual == 0 :
        divisores.append(numero_actual)

print(divisores) 