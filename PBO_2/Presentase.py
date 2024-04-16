try:
    nilai = float(input("Masukkan nilai: "))
    total = float(input("Masukkan total nilai: "))
    if total <= 0:
        raise ValueError("Total nilai harus positif")
    persentase = (nilai / total) * 100
    print("Persentase:", persentase, "%")
except ValueError as e:
    print("Error:", e)
except ZeroDivisionError:
    print("Error: Total nilai tidak boleh nol.")