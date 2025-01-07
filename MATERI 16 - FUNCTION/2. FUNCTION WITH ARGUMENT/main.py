# FUNGSI DENGAN ARGUMENT

# STRUKTUR FUNCTION

# def 'nama_function' ( parameter/argument ) :
#      badan function

def hello_world(nama) :
    print(f"haloo {nama}\n") # DATA DARI INPUT AKAN DI KELUARKAN DISINI

hello_world(input("Siapa Namamu? ")) # DATA DARI INPUT AKAN MASUK KE PARAMETER
#            ^^^^^^^^^^^^^^^^ SEMUA JENIS DATA (int, str, boolean, variable, list, dict, dll)
#                             DAPAT DI MASUKKAN DI PARAMETER, LALU DIBAWA KEATAS

# ======================================== #

def ngitung (num_1, num_2) :
    print(num_1 + num_2)

    for i in range(num_1 + num_2) :
        print(f"Angka ke = {i}")

ngitung (int(input("Angka: ")), int(input("Angka Kedua: ")))

# ======================================== #

def kelompok (nama_1, nama_2, nama_3) :

    data = [anggota_1, anggota_2, anggota_3]
    list_anggota.append(data)

    print("\nAnggota Kelompok mu Adalah: ")
    for i in data :
        print(f"Nama = {i}")

list_anggota = []

print("\n\nMasukkan 3 anggota kelompok")
anggota_1 = (input("Anggota 1: "))
anggota_2 = (input("Anggota 2: "))
anggota_3 = (input("Anggota 3: "))

kelompok(anggota_1, anggota_2, anggota_3)