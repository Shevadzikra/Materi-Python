# Write a program to create function func1() to accept a variable length of arguments and print their value.

'''call a function with 3 arguments'''
# func1(20, 40, 60)

'''call a function with 2 arguments'''
# func1(100, 200)

def func1(*args) :
    for i in args:
        print(i)

func1(20, 40, 60)
func1(100, 200)