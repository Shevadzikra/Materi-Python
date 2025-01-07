# PROGRAM LIST BUKU

list_buku = []
while True: 
    print("\nDATA BUKU")

    judul = input("Masukkan Judul Buku\t: ")
    penulis = input("Masukkan Penulis Buku\t: ")

    buku = [judul,penulis]
    list_buku.append(buku)

    print("\n\n", "="*10)
    for index,book in enumerate(list_buku):
        print(f"{index + 1} | {book[0]} | {book[1]}") 

    print("\n\n", "="*20)
    isLanjut = input("Apakah ingin lanjut? (y/n)")
    
    if isLanjut == "y":
        continue
    elif isLanjut == "n":
        break
    elif isLanjut != "n" or "y":
        print("Invalid")