#OPERASI LOGIKA DAN BOOLEAN

# not, or, and, xor

# NOT
print("====NOT====")
a = True
c = not a
print("data boolean =", a)
print("======= NOT")
print("data c =", c)

# OR ( jika salah satu adalah true, maka hasilnya adalah true )
print("====OR====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)

a = True
b = False
c = a or b
print(a, " OR", b, "=", c)

a = False
b = True
c = a or b
print(a, "OR", b, " =", c)

a = True
b = True
c = a or b
print(a, " OR", b, " =", c)

# AND ( jika dua buah nilai adalah true, maka hasilnya true )
print("====AND====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)

a = True
b = False
c = a and b
print(a, " AND", b, "=", c)

a = False
b = True
c = a and b
print(a, "AND", b, " =", c)

a = True
b = True
c = a and b
print(a, " AND", b, " =", c)

# XOR ( hanya dibutuhkan satu true, maka hasilnya true. dua true menghasilkan false sisanya false )
print("====XOR====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)

a = True
b = False
c = a ^ b
print(a, " XOR", b, "=", c)

a = False
b = True
c = a ^ b
print(a, "XOR", b, " =", c)

a = True
b = True
c = a ^ b
print(a, " XOR", b, " =", c)