import math

class Kerucut:
    def __init__(self):
        self.jari_jari = None
        self.tinggi = None
        self.volume = None

    def hitung_volume(self, jari_jari, tinggi):
        self.jari_jari = jari_jari
        self.tinggi = tinggi
        self.volume = (1/3) * math.pi * self.jari_jari ** 2 * self.tinggi
        return self.volume

K = Kerucut()
jari_jari = float(input("Masukkan jari-jari kerucut: "))
tinggi = float(input("Masukkan tinggi kerucut: "))
volume = K.hitung_volume(jari_jari, tinggi)

print("Jari-jari kerucut:", jari_jari)
print("Tinggi kerucut:", tinggi)
print("Volume Kerucut:", volume)