# DICTIONARY METHODS

# 1. clear()
# MENGHAPUS SEMUA ITEM DALAM DICT

print("METHOD clear()")
#    =>  "dictionary".clear()

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
    }

car.clear()

print(car)


# 2. copy()
# MEMBUAT DUPLIKAT DICT

print("\n\nMETHOD copy()")
#    =>  "dictionary".copy()

car = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
    }

x = car.copy()

print(x)


# 3. fromkeys()
#

print("\n\nMETHOD fromkeys()")
#    =>  "dictionary".fromkeys(keys, value)

x = ('key1', 'key2', 'key3')
y = 5

thisdict = dict.fromkeys(x, y)

print(thisdict)


# 4. get()
#

print("\n\nMETHOD get()")
#    =>  "dictionary".get('keyname', value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)


# 5. items()
# MENGAMBIL DATA ITEMS ( keys, values ) DALAM DICTIONARY

print("\n\nMETHOD items()")
#    =>  "dictionary".items()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x)


# 6. keys()
# MENGAMBIL DATA KEYS

print("\n\nMETHOD keys()")
#    =>  "dictionary".keys()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()

print(x)


# 7. pop()
# MENGAHPUS ITEM

print("\n\nMETHOD pop()")
#    =>  "dictionary".pop('keyname', defaultvalue)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.pop("model")

print(x)
print(car)


# 8. popitem()
# MENGHAPUS ITEM TERAKHIR

print("\n\nMETHOD popitem()")
#    =>  "dictionary".popitem()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.popitem()

print(car)
print(x)


# 9. setdefault()
# 

print("\n\nMETHOD setdefault()")
#    =>  "dictionary".setdefault('keyname', value)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
print(car)


# 10. update()
# 


print("\n\nMETHOD update()")
#    =>  "dictionary".update(iterable)
#                           A dictionary or an iterable object 
#                           with key value pairs, that will be 
#                           inserted to the dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})

print(car)


# 11. values()
# MENGAMBIL DATA VALUES

print("\n\nMETHOD values()")
#    =>  "dictionary".values()

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()

print(x)