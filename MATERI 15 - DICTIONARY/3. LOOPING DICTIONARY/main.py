# LOOPING DICTIONARY

person = {
    "bud" : "Budi",
    "jok" : "joko",
    "sam" : "Samsul",
    "sep" : "Asep"
}

# LOOPING [ yang keluar adalah key nya ]

for name in person :
    print(name)

print("\n")



# ====OPERATOR UNTUK MENGAMBIL ITEM / ITERABLE====


# HANYA MENGAMBIL KEY
keys = person.keys()
print(keys, "\n")

for key in person.keys() : 
    print(person.get(key))

print("\n")

# HANYA MENGAMBIL VALUE
values = person.values()
print(values)

print("\n")

for value in person.values() :
    print(value)

# MENGAMBIL ITEM [ key dan value ]

items = person.items()
print(items)

print("\n")

for item in person.items() : 
    print(item)

for key, value in person.items() :
    print(f"Key = {key} Value = {value}")