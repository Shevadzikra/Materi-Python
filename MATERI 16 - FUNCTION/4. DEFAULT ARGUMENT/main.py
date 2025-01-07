# DEFAULT ARGUMENT / PARAMETER

# def function( argument / parameter = nilai default ) :


def say_hello(text = "World") :
#                     ^^^^^ nilai default
    print(f"Hello {text}")

say_hello()


def greetings(name, message = "Apa Kabar?") : # BISA MENGGUNAKAN MULTI VARIABLE
    #                   ^^^^^^^^ VARIABLE DENGAN NILAI DEFAULT
    print(f"Hai {name}, {message}")

greetings(input("Siapa Namamu: "))
#         ^^^^^^ HANYA MENGISI VARIABLE {name}


# ===== BISA MENGAKSES VARIABLE DALAM FUNCTION =====

def math(num_1=1, num_2=2, num_3=3, num_4=4, num_5=5) :
    result = num_1 + num_2 + num_3 + num_4 + num_5

    return result

hasil = math(num_3 = 10) # MENGAKSES VARIABLE num_3
#                          lalu merubah nilai default = 10
print(hasil)