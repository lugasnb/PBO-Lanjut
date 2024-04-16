try:
    jumlah_data = int(input("Masukkan jumlah data: "))
    data = [float(input("Masukkan data ke-{}: ".format(i + 1))) for i in range(jumlah_data)]
    rata_rata = sum(data) / jumlah_data
    print("Rata-rata:", rata_rata)
except ValueError:
    print("Error: Masukan harus berupa angka.")
except ZeroDivisionError:
    print("Error: Tidak ada data untuk dihitung rata-ratanya.")