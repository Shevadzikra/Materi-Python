## OPERASI BITWISE, BINER, BINARY

a = 9
b = 5

# BITWISE or -> ( | )

c = a | b
print("\n=======OR=======")
print("nilai: ", a, "-> binary: ", format(a, '08b'))
print("nilai: ", b, "-> binary: ", format(b, '08b'))
print("===================================(|)")
print("nilai: ", c, "-> binary: ", format(c, '08b'))

# BITWISE and -> ( & )

c = a & b
print("\n\n=======AND=======")
print("nilai: ", a, "-> binary: ", format(a, '08b'))
print("nilai: ", b, "-> binary: ", format(b, '08b'))
print("===================================(&)")
print("nilai: ", c, "-> binary: ", format(c, '08b'))


# BITWISE xor -> ( ^ )

c = a ^ b
print("\n\n=======XOR=======")
print("nilai: ", a, "-> binary: ", format(a, '08b'))
print("nilai: ", b, "-> binary: ", format(b, '08b'))
print("===================================(^)")
print("nilai: ", c, "-> binary: ", format(c, '08b'))

# SHIFT RIGHT -> ( >> )

c = a >> 1
print("\n\n=======SHIFT RIGHT=======")
print("nilai: ", a, "-> binary: ", format(a, '08b'))
print("===================================(>>)")
print("nilai: ", c, "-> binary: ", format(c, '08b'))

# SHIFT LEFT -> ( << )

c = a << 1
print("\n\n=======SHIFT LEFT=======")
print("nilai: ", a, "-> binary: ", format(a, '08b'))
print("===================================(<<)")
print("nilai: ", c, "-> binary: ", format(c, '08b'))