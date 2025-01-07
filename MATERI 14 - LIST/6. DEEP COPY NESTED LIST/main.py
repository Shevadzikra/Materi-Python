
data_1 = [1,2]
data_2 = [3,4]

data = [data_1, data_2]
copy = data.copy()

print(f"data = {data}")
print(f"data copy = {copy}")

# MENGAMBIL DATA DARI NESTED LIST

pick = data[0][1]
print(f"data yang diambil = {pick}\n")

# ADDRESS SEMUA DATA

print(f"address data = {hex(id(data))}")
print(f"address data copy = {hex(id(copy))}")

from copy import deepcopy
