import datetime as dt
import os
import string
import random

template = {
    'nama': 'nama',
    'kelamin': 'kelamin',
    'lahir': 'lahir'
}

person = {}

while True:
    os.system("cls")
    DATA = dict.fromkeys(template.keys())

    DATA['nama'] = input("Masukkan Nama: ")
    DATA['kelamin'] = input("Masukkan Kelamin: ")

    Year = int(input("Masukkan Tahun: "))
    Month = int(input("Masukkan Bulan: "))
    Day = int(input("Masukkan Hari: "))

    DATA['lahir'] = dt.datetime(Year, Month, Day).strftime('%x')

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    person[KEY] = DATA

    print("\n\n")
    print(f"{'NAMA' :<13} {'KELAMIN' :<16} {'TANGGAL LAHIR' :<9}")
    print("=" * 60)

    for key, data in person.items():
        print(f"{data['nama']:<13} {data['kelamin']:<16} {data['lahir']:<9}")

    isLanjut = input("Apakah ingin lanjut? (y/n): ")
    
    if isLanjut.lower() == "y":
        continue
    elif isLanjut.lower() == "n":
        break
    else:
        print("Invalid input")
