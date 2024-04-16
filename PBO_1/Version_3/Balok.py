class Balok:
    def __init__(self):
        self._panjang = None
        self._lebar = None
        self._tinggi = None

    @property
    def panjang(self):
        return self._panjang

    @panjang.setter
    def panjang(self, value):
        self._panjang = value

    @property
    def lebar(self):
        return self._lebar

    @lebar.setter
    def lebar(self, value):
        self._lebar = value

    @property
    def tinggi(self):
        return self._tinggi

    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value

    def hitung_volume(self):
        return self._panjang * self._lebar * self._tinggi

# Contoh Penggunaan
B = Balok()
B.panjang = int(input("Masukkan nilai panjang balok: "))
B.lebar = int(input("Masukkan nilai lebar balok: "))
B.tinggi = int(input("Masukkan nilai tinggi balok: "))

V = B.hitung_volume()

print("Panjang:", B.panjang)
print("Lebar:", B.lebar)
print("Tinggi:", B.tinggi)
print("Volume Balok:", V)
