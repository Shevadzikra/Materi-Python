#LATIHAN KONVERSI SATUAN TEMPERATURE

#PROGRAM KONVERSI SATUAN CELCIUS KE SATUAN LAIN
print("\n============PROGRAM KONVERSI SATUAN============\n")

#celcius
celcius = float(input("masukkan suhu dalam celcius: "))
print("suhu adalah: ", celcius, "C") 

#reamur
reamur = (4/5) * celcius
print("suhu reamur adalah: ", reamur, "r")

#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu fahrenheit adalah: ", fahrenheit, "F")

#kelvin
kelvin = celcius + 273
print("suhu kelvin adalah: ", kelvin, "k")

#=======TUGAS=======#
print("\n#=======TUGAS=======#\n")

#konversikan fahrenheit ke kelvin
print("1. konversikan fahrenheit ke kelvin!")
Fahrenheit = float(input("masukkan suhu dalam Fahrenheit: "))
Kelvin = ((Fahrenheit - 32) * 5/9) + 273.15
print("suhu konversi adalah: ", Kelvin, "K") 

#konversikan kelvin ke fahrenheit
print("\n2. konversikan kelvin ke fahrenheit!")
KELVIN = float(input("masukkan suhu dalam Kelvin: "))
FAHRENHEIT = ((KELVIN - 273.15) * 9/5) + 32
print("suhu konversi adalah: ", FAHRENHEIT, "F")