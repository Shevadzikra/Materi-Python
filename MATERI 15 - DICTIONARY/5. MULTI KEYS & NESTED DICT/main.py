import datetime as dt

Mahasiswa1 = {
    "nama" : "Lavi",
    "nim" : '10084211',
    "sks_lulus" : 189,
    "beasiswa" : True,
    "lahir" : dt.date(2000, 8, 19)
}

Mahasiswa2 = {
    "nama" : "Marco",
    "nim" : '10098001',
    "sks_lulus" : 173,
    "beasiswa" : False,
    "lahir" : dt.date(2005, 1, 23)
}

Mahasiswa3 = {
    "nama" : "Alvaro",
    "nim" : '10009211',
    "sks_lulus" : 170,
    "beasiswa" : True,
    "lahir" : dt.date(2003, 6, 21)
}

data_Mahasiswa = {
    "MAH001" : Mahasiswa1,
    "MAH002" : Mahasiswa2,
    "MAH003" : Mahasiswa3
}

print(f"{"KEY" :<6} {"Nama" :<16} {"NIM" :<9} {"SKS" :<5} {"Beasiswa" :<10} {"Lahir" :<10}")
print("="*60)

for Mahasiswa in data_Mahasiswa : 
    
    KEY = Mahasiswa
    NAMA = data_Mahasiswa[KEY]['nama']
    NIM = data_Mahasiswa[KEY]['nim']
    SKS = data_Mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_Mahasiswa[KEY]['beasiswa']
    LAHIR = data_Mahasiswa[KEY]['lahir'].strftime('%x')

    print(f"{KEY :<6} {NAMA :<16} {NIM :<9} {SKS :<5} {BEASISWA:<10} {LAHIR :<10}")
