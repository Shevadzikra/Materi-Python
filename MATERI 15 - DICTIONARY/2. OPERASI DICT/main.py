# OPERASI DICTIONARY

data_dict = {
    "fr" : "Ferrari",       # 1
    "lb" : "Lamborghini",   # 2
    "dc" : "Duccati",       # 3
    "tl" : "Tesla"          # 4
}

# PANJANG DICTIONARY
LENDICT = len(data_dict)
print(f"panjang dictionary: {LENDICT}")

# MENGECEK key ADA ATAU TIDAK
KEY = "lb"
CHECK_KEY = KEY in data_dict
print(KEY, ":", CHECK_KEY)

# MENGAKSES VALUE MENGGUNAKAN get
print(data_dict["tl"])
print(data_dict.get("tl"))
print(data_dict.get("bl", "key tidak di temukan\n")) # cek key dengan message

# MENGUPDATE DATA
data_dict["fr"] = "Ford"
print(data_dict, "\n")

data_dict.update({"lb" : "Lambada"}) # JIKA DATA DALAM DICT ADA, MAKA INI AKAN MEMPERBARUI DATA DAN MENGUBAHNYA
data_dict.update({"ms" : "Mustang"}) # JIKA DATA DALAM DICT TIDAK ADA, MAKA INI AKAN DI TAMBAHKAN
print(data_dict, "\n")

# DELETE DATA DALAM DICTIONARY

del data_dict["dc"]
print(data_dict)