try:
    basis = float(input("Masukkan basis: "))
    eksponen = int(input("Masukkan eksponen (bilangan bulat): "))
    hasil = basis ** eksponen
    print("Hasil pangkat:", hasil)
except ValueError:
    print("Error: Masukan harus sesuai.")
