
# ALL LIST METHODS

# 1. append()
# MENAMBAHKAN ELEMENTS DI AKHIR LIST

print("METHOD append()")
#    =>  "list".append(element)

fruits = ["apple", "banana"]
fruits.append("mango")

a = ["mango", "melon", "papaya"]
b = ["BMW", "Ferrari"]
a.append(b)

print(fruits, "\n", a)


# 2. copy()
# MEMBUAT DUPLIKAT LIST

print("\n\nMETHOD copy()")
#    => "list".copy()

fruits = ["apple", "banana"]
x = fruits.copy()

print(x)


# 3. clear()
# MENGHAPUS SEMUA ITEM DIDALAM LIST

print("\n\nMETHOD clear()")
#   => "list".clear()

fruits = ["apple", "banana"]
fruits.clear()

print(f"data nya sudah dihapus: [{fruits}]")


# 4. count()
# MENGHITUNG ELEMEN DIDALAM LIST

print("\n\nMETHOD count()")
#   => "list".count(value)  |   (str,int,list,tuple, etc.)

fruits = ["apple", "banana", "banana"]
x = fruits.count("banana")

print(x)


# 5. extend()
# MENAMBAHKAN SETIAP ELEMEN DARI ITERABLE KE AKHIR DAFTAR 

print("\n\nMETHOD extend()")
#   => "list".extend(iterable)  |   (list,set,tuple,etc)

fruits = ["apple", "banana", "cherry"]
name = ["Budi","Joko"]

fruits.extend(name)

print(fruits)


# 6. index()
# MENGEMBALIKAN INDEX TERENDAH/PERTAMA TEMPAT ELEMENT MUNCUL

print("\n\nMETHOD index()")
#   => "list".index(element)  |   (str,int,list,etc)

fruits = ["apple", "banana", "cherry"]
x = fruits.index("banana")

print(x)


# 7. insert()
# MENYISIPKAN ELEMENT TERTENTU PADA INDEX TERTENTU DALAM LIST

print("\n\nMETHOD insert()")
#   => "list".insert(pos, element)  |  pos = posisi index   |   element = (str,int,object,etc)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "papaya")

print(fruits)


# 8. pop()
# MENGHAPUS & MENGEMBALIKAN NILAI TERAKHIR DARI DAFTAR atau NILAI INDEX YG DIBERIKAN

print("\n\nMETHOD insert()")
#   => "list".pop(pos)  |  pos = (OPSIONAL) default value yg dihapus -1 [paling akhir]

fruits = ["apple", "banana", "cherry"]
fruits.pop()

print(fruits)


# 9. remove()
# MENGHAPUS OBJECT TERTENTU DALAM LIST

print("\n\nMETHOD revome()")
#   => "list".remove(element)   |   (str,int,list,etc)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

print(fruits)


# 10. reverse()
# MEMBALIKKAN LIST

print("\n\nMETHOD reverse()")
#   => "list".reverse()

fruits = ["apple", "banana", "cherry"]
fruits.reverse()

print(fruits)


# 11. sort()
# MENGURUTKAN LIST - MENAIK > MENURUN atau DITENTUKAN OLEH USER

print("\n\nMETHOD sort()")
#   => "list".sort(reverse = True | False, key = myFunc)
# reverse (OPSIONAL) reverse = True - will sort the list descending    |    default:  reverse = False
# key (OPSIONAL). A function to specify the sorting criteria(s)

cars = ["BMW","Ford","Lambo"]
cars.sort

print(cars)

# 12. min()
# MENGHITUNG MINIMUM LIST

# 13. max()
# MENGHITUNG JUMLAH MAKSIMUM ELEMENT DALAM LIST