try:
    angka1 = float(input("Masukkan angka pertama: "))
    angka2 = float(input("Masukkan angka kedua: "))
    hasil = angka1 - angka2
    print("Hasil pengurangan:", hasil)
except ValueError:
    print("Error: Masukan harus berupa angka.")