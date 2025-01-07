''' *args '''

def fungsi(*args) :

    nama = args[0]
    tinggi = args[1]
    berat = args[2]

    return nama, tinggi, berat

data = fungsi("Budi", 170, 50)

print(data)

''' studi kasus '''