try:
    sisi = float(input("Masukkan angka sisi: "))
    hasil = sisi + sisi + sisi + sisi
    print("Hasil persegi:", hasil)
except ValueError:
    print("Error: Masukan harus berupa angka.")
