from random import randint

PIEDRA = 1
TIJERA = 2 
PAPEL = 3
Total_de_partidas = 5

def maquina():
    a = randint(1,3)
    return a

def usuario():
    b = 0
    while b not in range(1, 4):
        b = int(input('1=🗿 2=✂️  3=🧻?'))
    return b 

def funcion(n1,n2):
    if n1 == n2 :
        return(0)
    elif n1 == PIEDRA:
        return -1 if n2 == TIJERA else 1
    elif n1 == TIJERA:
        return -1 if n2 == PAPEL else 1
    else: # n1 == PAPEL
        return -1 if n2 == PIEDRA else 1

def valor(codigo):
    if codigo == PIEDRA:
        return f"PIEDRA"
    elif codigo == TIJERA:
        return f"TIJERA"
    else:
        return f"PAPEL"

if __name__ == "__main__":
    puntos_maquina = 0
    puntos_usuario = 0
    TOTAL_PARTIDAS = 2
    
    while puntos_usuario < TOTAL_PARTIDAS and puntos_maquina < TOTAL_PARTIDAS :
        
        jugada_usuario = usuario()
        jugada_maquina = maquina()

        print(f"Máquina: {valor(jugada_maquina)} - Humano: {valor(jugada_usuario)}")
        
        resultado = funcion(jugada_maquina,jugada_usuario) # ==> -1 ó 0 ó 1
        
        if resultado == -1:
            puntos_maquina = puntos_maquina + 1 
            print('Has perdido, HAHAHA!')
        elif resultado == 1:
            puntos_usuario = puntos_usuario + 1 
            print('Has ganado')
        else:
            print('Hemos empatado')

        
        print(f"Puntuación:Máquina: {puntos_maquina} - Humano: {puntos_usuario}")



