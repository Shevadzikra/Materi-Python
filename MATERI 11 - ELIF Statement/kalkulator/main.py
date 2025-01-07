# KALKULATOR DENGAN PYTHON

num1 = float(input())
operator = input()
num2 = float(input())

if operator == "+" :
    print("\n=", num1 + num2)
elif operator == "-" :
    print("\n=", num1 - num2)
elif operator == "*" :
    print("\n=", num1 * num2)
elif operator == "/" :
    print("\n=", num1 / num2)
else :
    print("\n= Invalid")