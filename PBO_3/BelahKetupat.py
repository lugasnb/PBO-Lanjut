class BelahKetupat:
    def __init__(self, sisi, diagonal1, diagonal2):
        self.__sisi = 0
        self.__diagonal1 = 0
        self.__diagonal2 = 0
        self.__setsisi (sisi)
        self.__setdiagonal1 (diagonal1)
        self.__setdiagonal2 (diagonal2)
        
    def getsisi(self):
        return self.__sisi
    
    def getdiagonal1(self):
        return self.__diagonal1
    
    def getdiagonal2(self):
        return self.__diagonal2

    def __setsisi (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__sisi = nilai

    def __setdiagonal1 (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__diagonal1 = nilai

    def __setdiagonal2 (self, nilai):
        if(nilai<=0):
            nilai = 1
        self.__diagonal2 = nilai

    def Luas (self):
        L = 1/2 * self.__diagonal1 * self.__diagonal2
        return L

    def Keliling(self):
        K = 4 * self.__sisi
        return K

try:
    sisi = int(input("Masukkan nilai Sisi:"))
    diagonal1 = int(input("Masukkan nilai Diagonal 1:"))
    diagonal2 = int(input("Masukkan nilai Diagonal 2:"))
except ValueError:
    print("Masukkan hanya angka saja")
else:
    B = BelahKetupat (sisi, diagonal1, diagonal2)
    L = B.Luas()
    K = B.Keliling()
    print("Sisi:", B.getsisi())
    print("Diagonal 1:", B.getdiagonal1())
    print("Diagonal 2:", B.getdiagonal2())
    print("Luas Belah Ketupat:", L)
    print("Keliling Belah Ketupat:", K)