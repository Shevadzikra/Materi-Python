
a = ["Mango","Banana","Apple"]
print(f"a = {a}")

b = a # PASS BY REFERENCE
print(f"b = {b} \n")


# MERUBAH MEMBER DARI a
# INI AKAN MERUBAH KEDUA LIST KARENA b = a [ADDRESS KEDUA LIST SAMA]
# KETIKA LIST b = a INI AKAN MEMBUAT LIST DENGAN MENGAMBIL ADDRESS DARI a
# SEHINGGA KETIKA MERUBAH DATA DARI SALAH SATU LIST, MAKA DATA DARI KEDUA LIST AKAN BERUBAH

a[1] = "Budi" 
b.sort()

print(f"a = {a}")
print(f"b = {b}")

# ADDRESS DARI KEDUA LIST
print(f"address dari a = {hex(id(a))}")
print(f"address dari b = {hex(id(b))} \n")

# ================================================= #

# MENDUPLIKAT LIST DENGAN copy

print("MEMBUAT LIST c DENGAN MENDUPLIKAT LIST a DENGAN a.copy()")

c = a.copy()
# INI AKAN MEMBUAT LIST BARU NAMUN DGN ADDRESS YG BERBEDA
# SEHINGGA KETIKA MERUBAH DATA LIST c, DATA DARI a DAN b TIDAK AKAN IKUT BERUBAH
# KARENA ADDRESS DARI LIST c SUDAH BERBEDA

print(f"address dari a = {hex(id(a))}")
print(f"address dari b = {hex(id(b))}")
print(f"address dari c = {hex(id(c))}")