try:
    angka1 = float(input("Masukkan angka pembilang: "))
    angka2 = float(input("Masukkan angka penyebut: "))
    hasil = angka1 / angka2
    print("Hasil pembagian:", hasil)
except ValueError:
    print("Error: Masukan harus berupa angka.")
except ZeroDivisionError:
    print("Error: Tidak dapat melakukan pembagian dengan nol.")