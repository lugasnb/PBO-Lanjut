import math

try:
    angka = float(input("Masukkan angka Positif: "))
    akar = math.sqrt(angka)
    print("Akar Kuadrat:", akar)
except ValueError:
    print("Error: Masukan harus berupa angka positif.")
