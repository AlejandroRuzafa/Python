a = int(input('numero 1 '))
b = int(input('numero 2 '))
c = int(input('numero 3 '))

if a > b :
    if b > c :
        print(c)
    else:
        print(b)
else:
    if a > c :
        print(c)
    else:
        print(a)
