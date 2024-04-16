try:
    input1 = float(input('Masukan angka pertama:'))
    input2 = float(input('Masukan angka kedua:'))
    hasil = input1 + input2
    print("Hasil penjumlahan:", hasil)
except ValueError:
    print("Error: Masukan harus berupa angka.")
except ZeroDivisionError:
    print("Error: Tidak dapat melakukan pembagian dengan nol.")