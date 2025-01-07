# 1. GAME TEBAK ANGKA DENGAN PYTHoN

guess_count = 0
guess_limit = 3
life = 3

while guess_count < guess_limit:
    print(f"Life Left: {life}")
    num = int(input("Guess: "))
    guess_count += 1

    if num == 5 :
        print("You Win! \n")

    else :
        if guess_count < guess_limit :
            print("Wrong Number! \n")
            life -= 1
            continue

        if guess_count == guess_limit :
             print("Wrong Number! \n")
             print("You Lose. Try Again! \n")

    if num == 5 :
        break


# 2. CAR GAME

i = 0
x = 1
started = False

while i < x : # KONDISI AWAL
    driver = input("Setir Mobilnya: ") # AKSI AWAL
     # i += 1 JIKA ADA SYNTAX INI, MAKA TIAP BLOCK HANYA AKAN DIJALANKAN 1X SAJA
     #        KARENA SUDAH MEMENUHI KONDISI [ i < x ]

    if driver == "start" :
        if started :
            print("mobil sudah dinyalakan! \n")
        else :
            started = True
            print("ready to start... go \n")

        #        JIKA TIDAK ADA AKSI [ i += 1 ] PROGRAM AKAN TERUS DIJALANKAN (LOOP)
        #        KARENA TIDAK ADA AKSI YANG DAPAT MEMENUHI KONDISI [ i < x ]

    else :
        if driver == "turn right" :
            if not started :
                print("mobil harus dinyalakan dahulu! \n")
            else :
                started = True
                print("mobil belok kanan \n")

        if driver == "turn left" :
            if not started :
                print("mobil harus dinyalakan dahulu! \n")
            else :
                started = True
                print("mobil belok kiri \n")

        if driver == "break" :
            if not started :
                print("mobil harus dinyalakan dahulu! \n")
            else :
                started = True
                print("nge rem mobil \n")
        
        if driver == "stop" :
            if not started :
                print("mobil sudah dimatikan! \n")
            else :
                started = False
                print("mobil dimatikan\n")

    if driver == "quit" :
        print("keluar mobil \n")
        break

    # ========================================================================= #
    # BERBEDA DENGAN SYNTAX INI

y = 0
z = 1

while y < z : # KONDISI AWAL
    driver = input("Setir Mobilnya Woy: ") # AKSI AWAL
    y += 1     # JIKA ADA SYNTAX INI, MAKA TIAP BLOCK HANYA AKAN DIJALANKAN 1X SAJA
               # KARENA SUDAH MEMENUHI KONDISI [ y < z ]

    if driver == "start" :
        print("ready to start... go \n")
        #        JIKA TIDAK ADA AKSI [ y += 1 ] PROGRAM AKAN TERUS DIJALANKAN (LOOP)
        #        KARENA TIDAK ADA AKSI YANG DAPAT MEMENUHI KONDISI [ y < z ]

    else :
        if driver == "turn right" :
            print("mobil belok kanan \n")

        if driver == "turn left" :
            print("mobil belok kiri \n")

        if driver == "break" :
            print("nge rem mobil \n")

    if driver == "quit" :
        print("keluar mobil \n")
        break