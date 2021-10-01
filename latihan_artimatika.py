# latihan konversi temperature
# program konvervi celcius ke satuan lain

print("\nProgram Konversi Temperatur")
celcius = float(input("masukan suhu dalam celcius : "))
print("suhu adalah ", celcius, " Celcius")

# reamur
# (4/5) * C
reamur = (4 / 5) * celcius
print("suhu dalam reamur", reamur, " Reamur")


# fahrenheit
fahrenheit = (9 / 5) * celcius + 32
print("suhu dalam fahrenheit", fahrenheit, " fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin", kelvin, " kelvin")