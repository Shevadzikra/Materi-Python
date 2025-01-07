# Pass

# pass hanya sebagai dummy -> tidak akan di execute

num = int(input("Masukkan Angka 1-5: "))

while num <= 5 :
    num += 1
    print(f"Angka Sekarang -> {num}") # Aksi 1

    if num == 3 :
        pass  # Akan membuat loop tidak di eksekusi
    
    print("Hallo") # Aksi 2