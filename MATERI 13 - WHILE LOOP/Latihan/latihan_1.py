# LATIHAN PERULANGAN MEMBUAT SEGITIGA

# 1. MENGGUNAKAN FOR
star = int(input("\n Masukkan Angka: "))
count = star

for i in range(star) :
    print("*"*count)
    count -= 1

    # =================================================================== #

# 2. MENGGUNAKAN WHILE
star = int(input("\n Masukkan Angka: "))
space = int(star % star)
count = 0
print("[ MEMBENTUK JAJAR GENJANG ]")

while True :
    count += 1
    print("*"*count)

    if count == star :
        break

while True :
    print(" "*space, "*"*count)
    count -= 1
    space += 1

    if count == 0 :
        break

        # =================================================================== #

# 3. HANYA MENCETAK ANGKA GANJIL
star = int(input("\n Masukkan Angka: "))
space = int(star/2)
count = 1
print("(HANYA MENCETAK ANGKA GANJIL)")
print("[ MEMBENTUK BELAH KETUPAT ]")

while True :
    if (count % 2 == 1) :
        print(" "*space, "*"*count)
        space -= 1
        count += 1
        
    else :
        count += 1
        continue

    if count >= star :
        break

while True :
    if (count % 2 == 1) :

        space += 1
        print(" "*space, "*"*count)
        count -= 1
        
    else :
        count -= 1

    if count == 0 :
        break

        # =================================================================== #
   
# 4. HANYA MENCETAK ANGKA GENAP
star = int(input("\n Masukkan Angka: "))
space = int(star/2)
count = 1
print("(HANYA MENCETAK ANGKA GENAP)")

while True :
    if (count % 2 == 0) :
        print(" "*space, "*"*count)
        space -= 1
        count += 1

    else :
        count += 1
        continue

    if count >= star :
        break
