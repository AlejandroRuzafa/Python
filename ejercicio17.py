
a = input('letra')

while len(a) != 1 :
    print('debe ser solo una letra')
    a = input('letra')

if a == 'i' or a =='a' or a =='e' or a =='o' or a =='u'  :
    print('es vocal')
else:
    print('no es vocal')