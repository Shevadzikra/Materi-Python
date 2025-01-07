# Continue

num = int(input("Masukkan Angka 1-5: "))

while num < 5 :
    num += 1
    print(f"Angka Sekarang -> {num}") # Aksi 1

    if num == 3 :
        print("World")
        continue  # Akan membuat loop meloncat ke step pertama

    print("Hallo") # Aksi 2