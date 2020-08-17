import datetime

now = datetime.datetime.now()
ano_actual = now.year


nombre = input("¿Cuál es tu nombre?")
edad = int(input("¿Cuál es tu edad?"))

nacimiento = ano_actual - edad 
años100 = nacimiento + 100
print(f"Cumplirás 100 años en {años100}")



