#  ===== LIST =====

# KUMPULAN DATA INT
num = [1,2,3,4,5,]
print(num, "\n")

# KUMPULAN DATA STR
string = ["apel","pisang","mangga"]
print(string, "\n")

# KUMPULAN DATA BOOLEAN
boolean = [True, False, False, True]
print(boolean, "\n")

# KUMPULAN DATA CAMPURAN
dataMix = [1,"apel", True, 2, "pisang", False]
print(dataMix, "\n")

# =========================== #

# CARA ALTERNATIF MEMBUAT LIST

dataRange = range(0, 10, 2) # range(start, stop, step)
print(dataRange)
dataList = list(dataRange)
print(dataList, "\n")

# LIST COMPREHENSION
# MEMBUAT LIST DENGAN FOR LOOP

data = [i**2 for i in range(0, 10)]
#        ^^ PANGKAT 2
print(data, "\n")

# FOR, IF LIST

data = [i for i in range(0, 10) if i % 2 == 0]
print(data) #             ^^^^^ MENCETAK ANGKA GENAP PADA RANGE 0 - 10
data = [i for i in range(0, 10) if i % 2 != 0]
print(data) #             ^^^^^ MENCETAK ANGKA GANJIL PADA RANGE 0 - 10