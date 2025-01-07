#OPERASI KOMPARASI|| SETIAP HASIL DARI OPERASI KOMPARASI ADALAH BOOLEANn (TRUE/FALSE)

# >, <, >=, <=, ==, !=, is, is not

x = 5
y = "10"

# > LEBIH BESAR DARI
print("======PROGRAM LEBIH BESAR DARI======")
result = x > 5
print(x, ">", 5, "=", result)
result = x > 2
print(x, ">", 2, "=", result)

# < KURANG DARI
print("======PROGRAM KURANG DARI======")
result = x < 1
print(x, "<", 1, "=", result)

# >= LEBIH BESAR DARI DAN SAMA DENGAN
result = x >= 5
print(x, ">=", 5, "=", result)

# <= KURANG DARI DAN SAMA DENGAN
result = x <= 1
print(x, "<=", 1, "=", result)

# != BUKAN DARI
result = x != 5
print(x, "!=", 5, "=", result)
result = x != 10
print(x, "!=", 10, "=", result)

# == SAMA DARI
result = y == 5
print(y, type(y), "==", 5, result)

result = 10 == 5
print(10, "==", 5, result)

result = x == 5
print(x, type(x), "==", 5, result)

# KOMPARASI {>, <, >=, <=, ==, !=} DAPAT BEKERJA PADA SYNTAX LITERAL
# SYNTAX LITERAL MAKSUDNYA SEBUAH SYNTAX YANG TIDAK MEMAKAN MEMORI
# SYNTAX NON LITERAL ; VARIABEL
# a = 5
# a (variabel akan memakan memori), 4 tidak memakan memori / literal

# "is" MEMBANDINGKAN OBJECT / MEMORY (KOMPARASI OBJECT IDENTITY)

a = 8
b = 8

result = a is b
print("a is b ", result)