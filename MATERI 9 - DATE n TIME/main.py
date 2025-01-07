#date and time 

import datetime as dt

today = dt.date.today()
print (today)

HBD = dt.date(2007,8,19)
print(HBD)

print("Silahkan masukkan tanggal lahir")
tahun = int(input("Tahun \t:"))
bulan = int(input("Bulan \t:"))
hari = int(input("Hari \t:"))

birth = dt.date(tahun,bulan,hari)
print(birth)
print(f"anda lahir pada hari: {birth:%A}")

today = today - birth
umur = today.days // 365
print("Hidup selama :", today)
print(f"Umur anda: {umur} tahun ")