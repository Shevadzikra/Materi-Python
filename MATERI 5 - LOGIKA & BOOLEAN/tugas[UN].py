# MASUKKAN ANGKA

# SOAL
# 1. ----- 0 +++++ 5 ----- 8 +++++ 11 -----

print("===== JAWABAN NO 1 =====")
inputUser = float(input("masukkan angka: "))

kurangNol = (inputUser < 0)
print("angka kurang dari 0: ",kurangNol)

antaraNolLima = (inputUser > 0 or inputUser < 5)
print("angka berada di antara nol dan lima: ", antaraNolLima)

antaraLimaDelapan = (inputUser < 5 and inputUser > 8)
print("angka berada di antara lima dan delapan: ",antaraLimaDelapan)

antaraDelapanSebelas = (inputUser > 8 and inputUser < 11)
print(antaraDelapanSebelas)

LebihSebelas = (inputUser > 11)
print(LebihSebelas)




# 2. +++++ 0 ----- 5 +++++ 8 ----- 11 +++++