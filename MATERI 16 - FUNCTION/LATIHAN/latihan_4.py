# Write a program to create a function show_employee() 
# using the following conditions.

# 1. It should accept the employee’s name and salary and display both.

# 2. If the salary is missing in the function call then 
#    assign default value 9000 to salary


'''EXPECTED OUTPUT'''
# Name: Ben salary: 12000
# Name: Jessa salary: 9000

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("Ben", 12000)
show_employee("Jessa")




