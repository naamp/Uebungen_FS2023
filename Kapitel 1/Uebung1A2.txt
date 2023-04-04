class WGS84Coord():
    def __init__(self, longitude=0, latitude=0):
        self.setKoord(longitude, latitude)
        
    def setKoord(self, longitude, latitude):
        if longitude <= -180 or longitude >= 180:
            raise ValueError("Die Longitude muss im Bereich von -180 und 180 sein.")
        if latitude <= -90 or latitude >= 90:
            raise ValueError("Die Laditude muss im Bereich von -90 und 90 sein.")
        self._longitude = longitude
        self._latitude = latitude
        
    def getKoord(self):
        return self._longitude, self._latitude
        
    def anzeigen(self):
        print("Longitude:", self._longitude)
        print("Latitude:", self._latitude)


K = WGS84Coord(60, 35)
K.anzeigen
