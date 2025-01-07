# COPY DICTIONARY

person = {
    'bud' : "Budi",
    "jok" : "Joko",
    "sep" : "Asep",
}

# friends = person | SAMA SEPERTI LIST JIKA HANYA SEPERTI INI,
#                    MAKA ADDRESS NYA AKAN SAMA

friends = person.copy()
friends["jok"] = "Joko Tarub"

print(f"Person = {person}\n")
print(f"Friends = {friends}\n")


# POP DICTIONARY [ berdasarkan key ]

Budi = friends.pop("bud")
print(f"{Budi}") # INI AKAN MENGAMBIL DATA DARI friends
print(friends, "\n") # SEHINGGA value = Budi DISINI AKAN DI AMBIL (hilang)
#                KARENA MENGGUNAKAN METHOD pop()


# POPITEM DICTIONARY

lastData = person.popitem() # MENGHAPUS ITEM TERAKHIR DALAM DICT
print(lastData) # LALU DI PANGGIL/AMBIL