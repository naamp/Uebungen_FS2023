class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):                                              #funktioniert
        return f"({self.x},{self.y},{self.z})"

    def __add__(self, other):                                       #funktioniert
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):                                       #funktioniert
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, other):
        if type(other) == Vector3:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif type(other) == float or type(other) ==int:
            return Vector3(self.x * other, self.y * other, self.z * other)
        
    def __rmul__(self, other):
        return Vector3(self.x * other, self.y * other, self.z * other)

    def __neg__(self):                                              #funktioniert
        return Vector3(-self.x, -self.y, -self.z)
    
    def __abs__(self):                                              #funktioniert
        return Vector3(abs(self.x), abs(self.y), abs(self.z))
    
    def length(self):
        return(self.x**2+self.y**2+self.z**2)**0.5
    
    def skalar(self, other):                                        #funktioniert
        return Vector3(self.x*other, self.y*other, self.z*other)

    def dot(self, other):                                           #funktioniert
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):                                         #funktioniert
        return Vector3((self.x * other.z)-(self.z * other.x), (self.z * other.x)-(self.x * other.z) , (self.x * other.y)-(self.y * other.x))
    
    def normalize(self):    
        betrag = (self.x**2+self.y**2+self.z**2)**0.5                                        #funktioniert
        return Vector3(self.x/betrag, self.y/betrag, self.z/betrag)
    

v1 = Vector3(1,2,3)
v2 = Vector3(3,4,5)
v4 = Vector3(10,10,10)

v5 = v1*2.5      #test komponentenweise Multiplikation
print(v5)

v13 = v1.skalar(5.359)  #test Skalarmultiplikation
print(v13)

v8=v1.dot(v4)   #test Skalarprodukt
print(v8)

v11=v1.cross(v4) #test Kreuzprodukt
print(v11)

v14=v1.normalize() #test Kreuzprodukt
print(v14)