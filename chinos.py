from random import randint

banca_ch = 0
banca_ch = randint(0,3)

def humano_ch():
    humano_ch = -1
    while humano_ch not in range(0, 4):
        humano_ch = int(input('cuantos sacas, 0 , 1, 2 o 3 '))
    return humano_ch 

def play_ch():
    a_ch = banca_ch + randint(0,3)
    return a_ch


fichas_humano_ch = humano_ch()
jugada_humano_ch = int(input('¿cuantas fichas crees que hay? '))
jugada_banca_ch = play_ch()
fichas_totales_ch = banca_ch + fichas_humano_ch
total_de_partidas_ch = 5 

for i in range(0,total_de_partidas_ch):
    print(f'¡En total hay {fichas_totales_ch} fichas! ')

    if jugada_humano_ch or jugada_banca_ch == fichas_totales_ch :
        if jugada_humano_ch == jugada_banca_ch :
            print('¡Hemos empatado!')
        elif jugada_humano_ch == fichas_totales_ch :
            print('¡Has ganado!')
        else :
            print('¡Has perdido HAHAHAAHA !')
    else :
        print('Ninguno ha acertado')

    print(f'Jugada banca = {jugada_banca_ch}')
    print(f'Tu jugada = {jugada_humano_ch}')

