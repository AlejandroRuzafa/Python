class Cafetera:
    def __init__(self, capacidad_agua):
        self.capacidad_agua = capacidad_agua
        self.tengo_agua = False
        self.tengo_cafe = False
        self.cafe_usado = False

    def __str__(self):
        tengo_agua = "estoy llena" if self.tengo_agua else "estoy vacia"
        tengo_cafe = "sí tengo cafe" if self.tengo_cafe else "no tengo café"
        return f"Soy una cafetera de {self.capacidad_agua} cl de capacidad, {tengo_agua} y {tengo_cafe}"
    
    def llenar_agua(self):
        self.tengo_agua = True

    def llenar_cafe(self):
        self.tengo_cafe = True
        self.cafe_usado = False

    def vaciar(self):
        self.tengo_agua = False
    
    def hacer_cafe(self):
        if self.tengo_agua and self.tengo_cafe and not self.cafe_usado:
            self.tengo_agua= False
            self.cafe_usado = True
            print( 'Cafe hecho' )
            return True 
        else:
            print ('me falta cafe y/o agua ')
            return False




cafetera_50 = Cafetera(50)
cafetera_100 = Cafetera(100)

print(cafetera_50)
print(cafetera_100)

cafetera_50.llenar_agua()
cafetera_50.llenar_cafe()
cafetera_50.hacer_cafe()

cafetera_50.llenar_agua()
cafetera_50.llenar_cafe()
cafetera_50.hacer_cafe()

cafetera_50.llenar_cafe()
cafetera_50.llenar_agua()
cafetera_50.hacer_cafe()
