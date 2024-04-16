class PersegiPanjang:

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

persegi_panjang = PersegiPanjang(7, 8)
luas = persegi_panjang.hitung_luas()

print("Luas persegi panjang:", luas)