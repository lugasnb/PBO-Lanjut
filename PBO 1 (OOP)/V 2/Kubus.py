class Kubus:
    def __init__(self):
        self.sisi = None
        self.volume = None

    def hitung_volume(self, sisi):
        self.sisi = sisi
        self.volume = self.sisi ** 3
        return self.volume

K = Kubus()
sisi = float(input("Masukkan panjang sisi kubus: "))
volume = K.hitung_volume(sisi)

print("Panjang sisi:", sisi)
print("Volume Kubus:", volume)
