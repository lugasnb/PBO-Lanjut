def faktorial(n):
    if n < 0:
        raise ValueError("Faktorial hanya didefinisikan untuk bilangan bulat positif")
    if n == 0:
        return 1
    else:
        return n * faktorial(n - 1)
try:
    angka = int(input("Masukkan angka faktorial: "))
    print("Faktorial dari", angka, ":", faktorial(angka))
except ValueError as e:
    print("Error:", e)
