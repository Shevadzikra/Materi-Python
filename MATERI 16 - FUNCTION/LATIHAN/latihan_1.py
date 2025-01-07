'''LATIHAN PYTHON'''

import os
os.system("cls")
# program menghitung luas dan keliling persegi panjang

print("=== PROGRAM MENGHITUNG KELILING DAN LUAS PERSEGI PANJANG ===")

def persegi_panjang(panjang, lebar) :
    K = 2 * (panjang + lebar)
    L = panjang * lebar

  #  print(f"\nKeliling = {K}")
  #  print(f"Luas = {L}\n")     > JIKA TIDAK MEMAKAI RETURN BISA DI PRINT DIDALAM  

    return K, L

result = persegi_panjang(int(input("\nMassukkan panjang: ")), int(input("Massukkan lebar: ")))

K, L = result # VARIABLE KELILING DAN LUAS HARUS DI DEFINISIKAN TERLEBIH DAHULU
#               DILUAR RETURN

print(f"\nKeliling = {K}")
print(f"Luas = {L}\n")
