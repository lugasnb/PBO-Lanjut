import math

class Tabung:
    def __init__(self):
        self._radius = None
        self._tinggi = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def tinggi(self):
        return self._tinggi

    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value

    def hitung_volume(self):
        return math.pi * self._radius ** 2 * self._tinggi

T = Tabung()
T.radius = int(input("Masukkan nilai radius tabung: "))
T.tinggi = int(input("Masukkan nilai tinggi tabung: "))

V = T.hitung_volume()

print("Radius:", T.radius)
print("Tinggi:", T.tinggi)
print("Volume Tabung:", V)
