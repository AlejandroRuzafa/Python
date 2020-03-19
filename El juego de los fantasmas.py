git init

git add .

git commit -m "first commit"
git remote add origin https://github.com/AlejandroRuzafa/galletitas-alemanas.git
git push -u origin master
# El juego de fantasmas
from random import randint
print ('El juego de fantasmas')
te_sientes_valiente = True
puntuacion = 0
while te_sientes_valiente:
    puerta_fantasma = randint(1, 3)
    print('Tres puertas ante ti...')
    print('un fantasma detras de una')
    print('¿Que puerta abres?')
    puerta = input('1, 2 o 3?')
    num_puerta = int(puerta)
    if num_puerta == puerta_fantasma:
        print('FANTASMA')
        te_sientes_valiente = False
    else:
        print('No hay fantasma')
        print('Entras a la habitacion siguiente')
        puntuacion = puntuacion + 1
print('¡Huye!')
print('Game over! Tu puntuacion es',puntuacion)
