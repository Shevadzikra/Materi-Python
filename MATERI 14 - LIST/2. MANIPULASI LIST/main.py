
# index   0(-3)    1(-2)    2(-1)
data = ["pepaya","mangga","pisang"]

# MENGAMBIL DATA DARI LIST
data_0 = data[0]
print(" \n"f"data pertama dalam list: {data_0}")
data_terakhir = data[-1]
print(f"data terakhir dalam list: {data_terakhir} \n")

# MENGAMBIL INFO PANJANG DATA DARI LIST
panjang_data = len(data)
print("panjang data: ", panjang_data, "\n")


# =================  MANIPULASI DATA LIST  ======================== #


# MENAMBAH ITEM PADA LIST SESUAI POSISI
print("data sebelum ditambah \n", data)

# "variabel".insert(posisi, item)
data.insert(1, "manggis")
print("data setelah ditambah \n", data)

# index          0(-4)    1(-3)     2(-2)     3(-1)
dataBerubah = ["pepaya","manggis", "mangga","pisang"] 
#             ^^^^^ MAKA DATA AKAN BERUBAH SEPERTI INI

# MENAMBAH DATA BARU DI BELAKANG
data.append("durian")
print("\ndata setelah ditambahkan di bagian belakang \n", data)


# MENAMBAH LIST DENGAN LIST
# data = ["pepaya","mangga","pisang"]
newData = ["BROKOLI","WORTEL","KANGKUNG","SAWI"]
data.extend(newData)
print("\ndata setelah digabung \n", data)

# ========================================================== #

# MERUBAH DATA
person = ["Asep", "Budi", "Joko"]
print("\ndata sebelum dirubah \n", person)
person[1] = "Michael"
print("data setelah dirubah \n", person)

# MENGHAPUS DATA [ remove ]
person.remove("Asep") # BESAR KECIL STRING HARUS SESUAI
print("\ndata setelah dihapus \n", person)

# MENGHAPUS DATA PALING BELAKANKG
person.pop()
print("\nsetelah data paling belakang dihapus \n", person)