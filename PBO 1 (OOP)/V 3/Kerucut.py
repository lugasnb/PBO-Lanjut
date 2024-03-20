import math

class Kerucut:
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
        return (1/3) * math.pi * self._radius ** 2 * self._tinggi

K = Kerucut()
K.radius = int(input("Masukkan nilai radius kerucut: "))
K.tinggi = int(input("Masukkan nilai tinggi kerucut: "))

V = K.hitung_volume()

print("Radius:", K.radius)
print("Tinggi:", K.tinggi)
print("Volume Kerucut:", V)
