
# 🗿  gana contra ✂️ y 🦎
# 🧻 gana contra 🗿 y  🖖
# ✂️ gana contra 🧻 y 🦎
# 🦎 gana contra 🖖 y 🧻
# 🖖 gana contra ✂️ y 🗿


from random import randint

PIEDRA = 1
TIJERA = 2 
PAPEL = 3
LAGARTO = 4
SPOCK = 5

def maquina():
    a = randint(1,5)
    return a

def usuario():
    b = 0
    while b not in range(1, 6):
        b = int(input('1=🗿 2=✂️  3=🧻 4=🦎 5=🖖 ?'))
    return b 

def funcion(n1,n2):
    if n1 == n2 :
        return(0)
    elif n1 == PIEDRA:
        if n2 == TIJERA or n2 == LAGARTO :
            return -1 
        elif n2 == PAPEL or n2 == SPOCK :
            return 1
    elif n1 == PAPEL:
        if n2 == PIEDRA or n2 == SPOCK :
            return -1 
        elif n2 == TIJERA or n2 == LAGARTO :
            return 1
    elif n1 == TIJERA:
        if n2 == PAPEL or n2 == LAGARTO :
            return -1 
        elif n2 == PIEDRA or n2 == SPOCK :
            return 1
    elif n1 == LAGARTO:
        if n2 == PAPEL or n2 == SPOCK :
            return -1 
        elif n2 == PIEDRA or n2 == TIJERA :
            return 1
    elif n1 == SPOCK:
        if n2 == PIEDRA or n2 == TIJERA :
            return -1 
        elif n2 == PAPEL or n2 == LAGARTO :
            return 1
    

def valor(codigo):
    if codigo == PIEDRA:
        return f"🗿"
    elif codigo == TIJERA:
        return f"✂️"
    elif codigo == PAPEL:
        return f"🧻"
    elif codigo == LAGARTO:
        return f"🦎"
    else:
        return f"🖖"  

if __name__ == "__main__":
    puntos_maquina = 0
    puntos_usuario = 0
    TOTAL_PARTIDAS = 5
    
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

    assert funcion(PIEDRA,PIEDRA) ==0
    assert funcion(PIEDRA,PAPEL) == 1
    assert funcion(PIEDRA,TIJERA) == -1
    assert funcion(PIEDRA,LAGARTO) == -1
    assert funcion(PIEDRA,SPOCK) == 1
    assert funcion(PAPEL,PIEDRA) == -1
    assert funcion(PAPEL,PAPEL) == 0
    assert funcion(PAPEL,TIJERA) == 1 
    assert funcion(PAPEL,LAGARTO) == 1 
    assert funcion(PAPEL,SPOCK) == -1 
    assert funcion(TIJERA,PIEDRA) == -1
    assert funcion(TIJERA,PAPEL) == -1
    assert funcion(TIJERA,TIJERA) == 0
    assert funcion(TIJERA,LAGARTO) == -1
    assert funcion(TIJERA,SPOCK) == 1
    assert funcion(LAGARTO,PIEDRA) == 1
    assert funcion(LAGARTO,PAPEL) == -1
    assert funcion(LAGARTO,TIJERA) == 1
    assert funcion(LAGARTO,LAGARTO) == 0
    assert funcion(LAGARTO,SPOCK) == -1
    assert funcion(SPOCK,PIEDRA) == -1
    assert funcion(SPOCK,PAPEL) == 1
    assert funcion(SPOCK,TIJERA) == -1
    assert funcion(SPOCK,LAGARTO) == 1
    assert funcion(SPOCK,SPOCK) == 0

