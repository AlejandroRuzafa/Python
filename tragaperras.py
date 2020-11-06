
f1 = ('🍒')
f2 = ('🍉')
f3 = ('🍍')
f4 = ('🍓')
f5 = ('🍌')
f6 = ('🥝')
f7 = ('🍇')
f8 = ('🥥')

z1 = ('🐢')
z2 = ('🐧')
z3 = ('🦍')
z4 = ('🦆')
z5 = ('🐦') 
z6 = ('🐫')
z7 = ('🐘')
z8 = ('🦅')

m1 = ('🐳')
m2 = ('🦈')
m3 = ('🐬')
m4 = ('🐙')
m5 = ('🐡')
m6 = ('🐠')
m7 = ('🐟')
m8 = ('🐚') 

e1 = ('🌌')
e2 = ('☀️')
e3 = ('🪐')
e4 = ('🌍')
e5 = ('🌙')
e6 = ('⭐')
e7 = ('☄️') 
e8 = ('🚀')

from random import randint

tipo_de_tragaperras = int(input('¿Que maquina quieres? 1 = 🍒 2 = 🐘 3 = 🐚 4 = 🌌  '))


def elegir_maquina():
    tipo_de_tragaperras = 0
    while tipo_de_tragaperras not in range(1, 4):
        tipo_de_tragaperras = int(input('¿Que maquina quieres? 1 = 🍒 2 = 🐘 3 = 🐚 4 = 🌌  '))
    return tipo_de_tragaperras 

Frutas = [f1,f2,f3,f4,f5,f6,f7,f8]
Animales = [z1,z2,z3,z4,z5,z6,z7,z8]
mar = [m1,m2,m3,m4,m5,m6,m7,m8]
espacio = [e1,e2,e3,e4,e5,e6,e7,e8]
final = []

def tirada_1(n):
    for randomm in range(0,3):
        randomm = randint(1,8)
        final.append(n[randomm])
    return final 

