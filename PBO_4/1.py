class Person:
    def __init__(self, full_name, gender):
        self.full_name = full_name
        self.gender = gender

class Dokter(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk

class Perawat(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk

class Karyawan(Person):
    def __init__(self, full_name, gender, nomor_induk):
        super().__init__(full_name, gender)
        self.nomor_induk = nomor_induk


asep = Dokter("Dr. Asep", "Laki-laki", "DOK001")
print("Nomor Induk:", asep.nomor_induk, ", Dokter:", asep.full_name, ", Jenis Kelamin:", asep.gender)


sitinur = Perawat("Siti Nur", "Perempuan", "PER001")
print( "Nomor Induk:", sitinur.nomor_induk, ", Perawat:", sitinur.full_name, ", Jenis Kelamin:", sitinur.gender)

budisantoso = Karyawan("Budi Santoso", "Laki-laki", "KAR001")
print("Nomor Induk:", budisantoso.nomor_induk, ", Karyawan:", budisantoso.full_name, ", Jenis Kelamin:", budisantoso.gender)
