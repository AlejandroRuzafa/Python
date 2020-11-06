#from random import randint
#
#numeros_negros = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,29,31,33,35]
#numeros_rojos  = [1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36]
#
#def rojo(n):
#    if n in numeros_rojos:
#        return True
#
#apuesta_r = 0
#while apuesta_r not in range(1, 6):
#    apuesta_r = int(input('¿A que quieres apostar? 1 = color 2 = par o impar 3 = numero 4 = mitad 5 = tercio '))
#
#resultado_ruleta = randint(0,36)
#
#def decir_numero():
#    if rojo(resultado_ruleta):
#        print(f'{resultado_ruleta},Rojo')
#    elif resultado_ruleta == 0 :
#        print('0,Verde')
#    else:
#        print(f'{resultado_ruleta},Negro')
#
#if apuesta_r == 1 :
#    apuesta_color = 0
#    while apuesta_color not in range(1, 3):
#        apuesta_color = int(input('1 = Rojo 2 = Negro'))
#    if apuesta_color == 1:
#        if rojo(resultado_ruleta):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas} fichas ')
#
#        else:
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#    else:
#        if not rojo(resultado_ruleta):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas} fichas ')
#        else :
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#if apuesta_r == 2 :
#    apuesta_par = 0
#    while apuesta_par not in range(1, 3):
#        apuesta_par = int(input('1 = Par 2 = Impar '))
#    if apuesta_par == 1:
#        if resultado_ruleta % 2 == 0 :
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas} fichas ')
#        else:
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#    else:
#        if resultado_ruleta % 2 != 0 :
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas} fichas ')
#        else :
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#if apuesta_r == 3 :
#    apuesta_numero = 0
#    while apuesta_numero not in range(0, 37):
#        apuesta_numero = int(input('pon el numero al que quieras apostar del 0 al 36'))
#    if apuesta_numero == resultado_ruleta :
#        fichas = fichas + (fichas_apostadas * 36)
#        decir_numero()
#        print(f'has ganado {fichas_apostadas * 35 } fichas ')
#if apuesta_r == 4 :
#    apuesta_mitad = 0 
#    while apuesta_mitad not in range(1,3):
#        apuesta_mitad = int(input('1 = del 1 al 18  2 = del 19 al 36'))
#    if apuesta_mitad == 1:
#        if resultado_ruleta in range(1,19):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas} fichas ')
#        else:
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#    else:
#        if resultado_ruleta in range(19,37):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas} fichas ')
#        else:
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#else:
#    apuesta_tercio = 0 
#    while apuesta_tercio not in range(1,4):
#        apuesta_tercio = int(input('1 = del 1 al 12  2 = del 12 al 24 3 = del 24 al 36'))
#    if apuesta_tercio == 1 :
#        if resultado_ruleta in range(1,13):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas * 2} fichas ')
#        else :
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#    if apuesta_tercio == 2 :
#        if resultado_ruleta in range(13,25):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas * 2} fichas ')
#        else :
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ')
#    else:
#        if resultado_ruleta in range(24,37):
#            fichas = fichas + (fichas_apostadas * 2)
#            decir_numero()
#            print(f'has ganado {fichas_apostadas * 2} fichas ')
#        else :
#            decir_numero()
#            print(f'has perdido {fichas_apostadas} fichas ') 