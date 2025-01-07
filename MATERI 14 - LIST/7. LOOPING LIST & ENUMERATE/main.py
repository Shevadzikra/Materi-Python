# LOOPING DARI LIST

# FOR LOOP
print("MENGGUNAKAN FOR LOOP")

num = [4,3,6,7,1,2]

for angka in num:
    print(f"angka = {angka}")

angka_kuadrat = [i**2 for i in num]
print(angka_kuadrat)

# FOR LOOP DAN RANGE
print("\nMENGGUNAKAN FOR LOOP DAN WHILE")

num = [1,2,3,4,5]

panjang = len(num)

for i in range(panjang):
    print(f"angka = {num[i]}")


# WHILE LOOP
print("\nMENGGUNAKAN WHILE LOOP")

num = [1,2,3,4,5]

panjang = len(num)
i = 0

while i < panjang:
    print(f"angka = {num[i]}")
    i += 1


# MENGGUNAKAN LIST COMPREHENSION
print("\n MENGGUNAKAN LIST COMPREHENSION")

data = ["Budi", 1, 2, 3, "Joko"]
[print(i) for i in data]


# ENUMERATE
print("\nENUMERATE")

data_list = ["Budi", 1, 2, 3, "Joko"]

for index,data in enumerate(data_list): 
    print(f"index = {index}, data = {data}")