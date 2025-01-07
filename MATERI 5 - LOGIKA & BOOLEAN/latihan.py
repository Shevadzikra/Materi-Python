# LATIHAN KOMPARASI DAN LOGIKA

# MEMBUAT GABUNGAN AREA RENTANG DARI ANGKA

#+++++++3---------10++++++++
#  TRUE    FALSE      TRUE

inputUser = float(input("masukkan angka yang bernilai \nkurang dari 3 \natau \nlebih besar dari 10\n: "))

# ++++++3---------------
# MEMERIKSA ANGKA KURANG DARI 3

isLessThan = (inputUser < 3)
print(isLessThan)

# ------10++++++++++++++
# MEMERIKSA ANGKA LEBIH DARI 20
isMoreThan = (inputUser > 10)
print(isMoreThan)

# +++++3--------10++++++
# MEMERIKSA ANGKA ANTARA 3 SAMPAI 10
isBetween = (inputUser < 3 and inputUser > 10)
print(isBetween)

# -------3++++++10-------
# KASUS IRISAN 
isBetween = (inputUser > 3 or inputUser < 10)
print(isBetween)

Message = print("Howdy !")