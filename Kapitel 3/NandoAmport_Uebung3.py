import math

class Figur: 
    def __init__(self, name): 
        self.name = name
        self._flaeche = 0
        self._umfang = 0

    def umfang(self):
        return self._umfang
    
    def flaeche(self):
        return self._flaeche
    
    def __str__(self):
        return self.name

#---------------------------------------------------------------
    
class Punkt(Figur):
    def __init__(self, x, y):
        super().__init__("Punkt")
        self.x = x
        self.y = y

    def __str__(self):
        return f"Punkt({self.x},{self.y})"
    
#-------------------------------------------------------------

class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__("Kreis")
        self.mittelpunkt = mittelpunkt
        self.radius = radius

    def flaeche(self):
        return self.radius**2 * math.pi
    
    def umfang(self):
        return self.radius * 2 * math.pi

    def __str__(self):
        return f"Kreis M = {self.mittelpunkt},r = {self.radius}"  
    
#-------------------------------------------------------------

class Dreieck(Figur):
    def __init__(self, A, B, C):
        super().__init__("Dreieck")
        self.A = A
        self.B = B
        self.C = C
        self._flaeche = self.dreieck_flaeche()
        self._umfang = self.dreieck_umfang()

    def dreieck_flaeche(self):          #mit Kreuzprodukt
        ab = [self.B.x - self.A.x, self.B.y - self.A.y]
        ac = [self.C.x - self.A.x, self.C.y - self.A.y]
        return abs(ab[0] * ac[1] - ab[1] * ac[0])
    
    def dreieck_umfang(self):
        ab = [self.B.x - self.A.x, self.B.y - self.A.y]
        ac = [self.C.x - self.A.x, self.C.y - self.A.y]
        bc = [self.C.x - self.B.x, self.C.y - self.B.y]
        return abs((ab[0] + ab[1])**2 + (ac[0] + ac[1])**2 + (bc[0] + bc[1])**2)

    def __str__(self):
        return f"Dreieck = {self.A} / B = {self.B} / C = {self.C}" +\
                f"Fläche = {self.dreieck_flaeche}"
    
class Rechteck(Figur):
    def __init__(self, A, C,):
        super().__init__("Rechteck")
        self.A = A
        self.C = C
      
    

#EIN- und AUSGABE

M = Punkt(2,3)
k1 = Kreis(M, 10)
P1 = Punkt(4,6)
P2 = Punkt(5,-2)
P3 = Punkt(-3,9)
D1 = Dreieck(M,P2,P3)

print(k1)
print(k1.flaeche())
print(k1.umfang())

print(D1)
print(D1.flaeche())
print(D1.umfang())
print(P3)
