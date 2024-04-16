class KonversiSuhu:

    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

suhu_celsius = 28
konversi = KonversiSuhu(suhu_celsius)
fahrenheit = konversi.to_fahrenheit()

print("Suhu dalam Fahrenheit:", fahrenheit)