# Erstellen Sie eine Klasse "Vector3", welche einen dreidimensionalen Vektor repräsentiert.
# Über den Konstruktor werden die Komponenten x, y und z definiert. Wird nichts angegeben, so wird ein Null-Vektor erstellt.
# Entwickeln Sie eine Methode len, welche die Länge des Vektors berechnet.
# Mit einer Instanz von Vector3 soll die Klasse getestet werden.

class Vector3: 
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def len(self):
        return ((self.x)**2 + 
                (self.y)**2 + 
                (self.z)**2)**0.5 

v1 = Vector3(3,4,5)

laenge = v1.len()
print(laenge)
