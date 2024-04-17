class Person:
    def __init__(self, full_name, gender):
        self.full_name = full_name
        self.gender = gender

class Dosen(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk

class Mahasiswa(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk

class Staff(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk

class Satpam(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk

class OB(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk


ahmad = Dosen("Ahmad, M,Kom", "Laki-laki", "DSN001")
print("NIM:", ahmad.nomor_induk, ", Dosen:", ahmad.full_name, ", Jenis Kelamin:", ahmad.gender)

rinaindah = Mahasiswa("Rina rinaindah", "Perempuan", "MHS001")
print("NID:", rinaindah.nomor_induk, ", Mahasiswa:", rinaindah.full_name, ", Jenis Kelamin:", rinaindah.gender)

budiraharjo = Staff("Budi Raharjo", "Laki-laki", "STF001")
print("NIP:", budiraharjo.nomor_induk, ", Staff:", budiraharjo.full_name, ", Jenis Kelamin:", budiraharjo.gender)

suryawijaya = Satpam("Surya Wijaya", "Laki-laki", "SAT001")
print("NIP:", suryawijaya.nomor_induk, ", Satpam:", suryawijaya.full_name, ", Jenis Kelamin:", suryawijaya.gender)

andisusanto = OB("Andi Susanto", "Laki-laki", "OB001")
print("NIP:", andisusanto.nomor_induk, ", Office Boy:", andisusanto.full_name, ", Jenis Kelamin:", andisusanto.gender)
