
num1 = [1,2]
num2 = [3,4]

dataNumber = [1,2,3,4]

print(f"data list biasa {dataNumber} \n")

# LIST DALAM LIST

listGabungan = [num1, num2, "Budi", 10]
print(listGabungan)

num3 = [4,5,6]
num3.pop()
num4 = [7,8]

listPop = [num3, num4]
print(listPop, "\n")

# CONTOH PENGGUNAAN
# DIGUNAKAN PADA DATA BERSERI

peserta_1 = ["Budi", 15, "Laki-laki"]
peserta_2 = ["Aca", 12, "Perempuan"]
peserta_3 = ["Joko", 11, "Laki-laki"]

list_peserta = [peserta_1, peserta_2, peserta_3]

print(list_peserta)

# SETELAH DI SORT
list_peserta.sort()
print("\nLIST SETELAH DI SORT\n", list_peserta)

# MENGAMBIL DATA DARI LIST

for peserta in list_peserta :
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"gender\t: {peserta[2]}\n")
