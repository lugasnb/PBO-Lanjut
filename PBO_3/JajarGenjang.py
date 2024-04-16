class JajarGenjang:
    def __init__(self, alas, sisimiring, tinggi):
        self.__alas = 0
        self.__sisimiring = 0
        self.__tinggi = 0
        self.__setalas (alas)
        self.__setsisimiring (sisimiring)
        self.__settinggi (tinggi)
        
    def getalas(self):
        return self.__alas
    
    def getsisimiring(self):
        return self.__sisimiring
    
    def gettinggi(self):
        return self.__tinggi
    
    def __setalas (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__alas = nilai

    def __setsisimiring (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__sisimiring = nilai

    def __settinggi (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__tinggi = nilai

    def Luas (self):
        L = self.__alas * self.__tinggi
        return L

    def Keliling(self):
        K = 2 * (self.__alas + self.__sisimiring)
        return K

try:
    alas = int(input("Masukkan nilai Alas:"))
    sisimiring = int(input("Masukkan nilai Sisi Miring:"))
    tinggi = int(input("Masukkan nilai Tinggi:"))
except ValueError:
    print("Masukkan hanya angka saja")
else:
    J = JajarGenjang (alas, sisimiring, tinggi)
    L = J.Luas()
    K = J.Keliling()
    print("Alas:", J.getalas())
    print("Sisi Miring:", J.getsisimiring())
    print("Tinggi:", J.gettinggi())
    print("Luas Jajar Genjang:", L)
    print("Keliling Jajar Genjang:", K)