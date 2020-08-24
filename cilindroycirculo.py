pi = 3.14159265359


def area_circulo(r):
    area= r ** 2 * pi
    return area

def perimetro_circulo(r):
    perimetro = 2 * pi * r 
    return perimetro

def area_cilindro(r,h):
    area_base = area_circulo(r)
    lado = perimetro_circulo (r)
    area_lateral = lado * h
    area = area_lateral + 2 * area_base
    return area 




    