# RETURN

# STRUKTUR FUNCTION dengan return

# def 'nama_function' ( parameter/argument ) :
#      badan function
#      return output

def kuadrat(x) :
    result = x**2
    
    return result
    # ^^ maksudnya data akan di keluarkan / di ambil

num = kuadrat(int(input("Masukkan Angka: ")))

print(num)


# BISA DENGAN BANYAK RETURN

def ngitung(x, y) :
    tambah = x + y
    kurang = x - y
    bagi = x / y
    kali = x * y

    return tambah, kurang, bagi, kali

# num_1 = int(input("Masukkan Angka Pertama: "))
# num_2 = int(input("Masukkan Angka Kedua: "))

hasil = ngitung(int(input("Masukkan Angka Pertama: ")), int(input("Masukkan Angka Kedua: ")))
print(hasil)




# RETURN BISA DI SEDERHANAKAN SEPERTI INI

def ngitung(x, y) :
   return x + y, x - y, x / y, x * y

# num_1 = int(input("Masukkan Angka Pertama: "))
# num_2 = int(input("Masukkan Angka Kedua: "))

hasil = ngitung(int(input("Masukkan Angka Pertama: ")), int(input("Masukkan Angka Kedua: ")))
print(hasil)