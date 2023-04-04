class WGS84Coord():
    def __init__(self, lng=0, lat=0):
        self.setLongitude(lng)
        self.setLatitude(lat)

    def setLongitude(self, lng):
       self._lng = lng 
        
    def setLatitude(self, lat):
        if lat > 90:
            self._lat = 90 - (lat-90)
        elif lat < -90:
            self._lat = -90 - (lat + 90)
        else:
            self._lat = lat
        
    def getLongitude(self):
        return self._lng
        
    def getLatitude(self):
        return self._lat    
    
    def anzeigen(self):
        print("Longitude:", self._lng)
        print("Latitude:", self._lat)


K = WGS84Coord(60, 35)
K.anzeigen

