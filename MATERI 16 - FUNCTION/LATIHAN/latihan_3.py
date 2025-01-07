# Write a program to create function calculation() 
# such that it can accept two variables and calculate 
# addition and subtraction. Also, it must return both addition 
# and subtraction in a single return call.

'''EXPECTED OUTPUT'''
# 50, 30


def calculation(a, b):
    num_1 = a + 10
    num_2 = b + 20

    return num_1, num_2

res = calculation(40, 10)
print(res)