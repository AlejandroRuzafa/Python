#Suma de los terminos de una progresion geometrica

r = float(input('¿r?'))
a = float(input('¿a1?'))
an = float(input ('¿an?'))

#if r < 1.0 and -1.0 < r :
if -1.0 < r < 1.0 :
    print (a /(1.0-r))
else :
    print ((an * r-a)/(r-1.0))
    
