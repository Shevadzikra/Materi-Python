import datetime as dt
import os
import string
import random

template = {
    'nama' : 'nama',
    'kelamin' : 'kelamin',
    'lahir' : 'lahir'
}

person = {}


while True :
    os.system("cls")
    DATA = dict.fromkeys(template.keys())

    DATA['nama'] = input("Masukkan Nama: ")
    DATA['kelamin'] = input("Masukkan Kelamin: ")

    Year = int(input("Masukkan Tahun: "))
    Month = int(input("Masukkan Bulan: "))
    Day = int(input("Masukkan Hari: "))

    DATA['lahir'] = dt.datetime(Year, Month, Day).strftime('%x')

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    person.update({KEY : DATA})

    print("\n\n")
    print(f"{"NAMA" :<13} {"KELAMIN" :<16} {"TANGGAL LAHIR" :<9}")
    print("="*60)

    for DATA in person :
        KEY = DATA
        NAMA = person[KEY]['nama']
        KELAMIN = person[KEY]['kelamin']
        BIRTH = person[KEY]['lahir']

    isLanjut = input("Apakah ingin lanjut? (y/n)")
    
    if isLanjut == "y":
        continue
    elif isLanjut == "n":
        break
    elif isLanjut != "n" or "y":
        print("Invalid")









#Kelamin = input("Masukkan Kelamin: ")
#Usia = input("Masukkan Usia: ")

#Year = int(input("Masukkan Tahun"))
#Month = int(input("Masukkan Bulan"))
#Day = int(input("Masukkan Hari"))

#Lahir = dt.datetime(Year, Month, Day)