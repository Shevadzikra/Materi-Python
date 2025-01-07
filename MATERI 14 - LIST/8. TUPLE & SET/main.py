# TUPLES
# FUNGSI TUPLE MEMBUAT LIST DENGAN DATA KONSTAN [TIDAK BISA DI UBAH]


data_tuples = (1,2,3,4,5)
print(data_tuples)
print(data_tuples[0])

# TIDAK BISA DI LAKUKAN DENGAN
# data_tuples[1] = "Budi"       TIDAK BISA MERUBAH DATA DALAM TUPLES
# data_tuples.append()          TIDAK BISA MENGGUNAKAN METHOD | ATTRIBUTE


# SETS
# SEBUAH DATA COLLECTION YANG TIDAK PUNYA INDEX

data_sets = {"budi", "joko", "micel"}
print(data_sets)

# BISA MENGGUNAKAN SEBAGIAN METHOD
data_sets.pop()
print(data_sets)

# TIDAK BISA MENGAMBIL DATA [index]
print(data_sets[1])
