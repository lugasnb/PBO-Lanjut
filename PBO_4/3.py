class Person:
    def __init__(self, full_name, gender):
        self.full_name = full_name
        self.gender = gender

class Manager(Person):
    def __init__(self, full_name, gender, employee_id):
        super().__init__(full_name, gender)
        self.employee_id = employee_id

class Programmer(Person):
    def __init__(self, full_name, gender, employee_id):
        super().__init__(full_name, gender)
        self.employee_id = employee_id

class Teknisi(Person):
    def __init__(self, full_name, gender, employee_id):
        super().__init__(full_name, gender)
        self.employee_id = employee_id

class Staff(Person):
    def __init__(self, full_name, gender, employee_id):
        super().__init__(full_name, gender)
        self.employee_id = employee_id


manager1 = Manager("Budi Santoso", "Laki-laki", "MGR001")
print( "Nomor Induk:", manager1.employee_id, ", Manager:", manager1.full_name, ", Jenis Kelamin:", manager1.gender)

programmer1 = Programmer("Rina Indah", "Perempuan", "PROG001")
print("Nomor Induk:", programmer1.employee_id, ", Programmer:", programmer1.full_name, ", Jenis Kelamin:", programmer1.gender)

teknisi1 = Teknisi("Surya Wijaya", "Laki-laki", "TEK001")
print("Nomor Induk:", teknisi1.employee_id, ", Teknisi:", teknisi1.full_name, "Jenis Kelamin:", teknisi1.gender)

staff1 = Staff("Andi Susanto", "Laki-laki", "STF001")
print("Nomor Induk:", staff1.employee_id, ", Staff:", staff1.full_name, ", Jenis Kelamin:", staff1.gender)
