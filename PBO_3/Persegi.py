class Persegi:
    def __init__(self, sisi):
        self.__sisi = 0
        self.__setsisi (sisi)
        
    def getsisi(self):
        return self.__sisi

    def __setsisi (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__sisi = nilai

    def Luas (self):
        L = self.__sisi * self.__sisi
        return L

    def Keliling(self):
        K = self.__sisi + self.__sisi + self.__sisi + self.__sisi
        return K

try:
    sisi = int(input("Masukkan nilai Sisi:"))
except ValueError:
    print("Masukkan hanya angka saja")
else:
    P = Persegi (sisi)
    L = P.Luas()
    K = P.Keliling()
    print("Sisi:", P.getsisi())
    print("Luas Persegi:", L)
    print("Keliling Persegi:", K)