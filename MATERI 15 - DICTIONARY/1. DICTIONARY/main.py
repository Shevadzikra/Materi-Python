# LIST
# DI AKSES MENGGUNAKAN index

data_list = ["Budi", "Joko", "Bagas"]

print(data_list[2], "\n\n")
             # ^^   index


# DICTIONARY (dict) -> ASSOCIATIVE ARRAY
# DI AKSES MENGGUNAKAN identifier => key

# tidak perlu menggunakan index seperti list / array
data = {
   # "key" : "value"
    "cars" : "BMW",
    "sports" : "Football"
}

data_dict = {
 # "key" : "value"
    "bd" : "Budi",
    "jk" : "Joko",
    "bg" : "Bagas",
    "num" : 123,
    "list" : data_list,
    "dict" : data
}

print(data_dict["bg"])
print(data_dict["num"])
print(data_dict["list"])
print(data_dict["dict"])

