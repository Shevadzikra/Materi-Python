# IF ELSE STATEMENT

name = input("Siapa namamu :")

# previous proggram
# if = kondisi : aksi
# next proggram

if name=="Lavi":
    print(f"Salam kenal {name}\n")
else:
    print("kamu bukan Lavi ya?\n")

umur = int(input("Masukkan umur: "))

#========================

if umur >= 18 :
    print("Kamu sudah dewasa\n")
else :
    print(f"kamu masih bocil, umurmu {umur}\n")

#========================

tahun = int(input("kamu lahir pada tahun berapa? "))

if tahun >= 2005 or tahun <= 2007 :
    print("kamu masih di jenjang SMA atau SMK\n")
else :
    print("mungkin kamu masih SD atau SMP atau mungkin sudah lulus\n")

#========================

import datetime as dt

year = int(input("Masukkan tahun: "))
month = int(input("Masukkan bulan: "))
day = int(input("Masukkan hari: "))

birth = dt.date(year,month,day)

if birth > dt.date(1945,8,17) :
    print(f"Tanggal lahirmu adalah: {birth}\n Artinya kamu lahir setelah Indonesia merdeka")
else :
    print("Mungkin kamu lahir sebelum indonesia merdeka")
    