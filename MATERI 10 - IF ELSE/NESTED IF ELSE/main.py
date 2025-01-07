# NESTED IF ELSE

# 1.
nilai = int(input("Masukkan nilai ulanganmu: "))

if nilai >= 90 : # mengecek daerah nilai apakah sama/lebih dari 90
   print("A\n")
else :
   if nilai >= 80 : # mengecek daerah nilai apakah sama/lebih dari 80
      print("B\n")
   else:
      if nilai >= 70 : # mengecek daerah nilai apakah sama/lebih dari 70
         print('C\n')
      else :              # jika daerah nilai dibawah 70, maka mencetak D
         print("D\n")

# 3.

umur = int(input("Masukkan Umur: "))

if umur <= 12 :
   print("Bocil\n")
else :
   if umur <= 18 :
      print("Remaja\n")
   else:
      if umur <= 30 :
         print("Dewasa\n")
      else :
         print("Sepuh\n")


# 3. MENGECEK APAKAH BILANGAN ITU GENAP/GANJIL DAN BILANGAN KELIPATAN 5/BUKAN
num = int(input("Masukkan bilangan: "))

if num % 2 == 0 :
   print("Bilangan Genap")
   if num % 5 == 0 :   # KONDISI INI AKAN DIJALANKAN JIKA KONDISI DIATAS TERPENUHI (JIKA BILANGAH YANG DIMASUKKAN GENAP )
      print("dan merupakan bilangan kelipatan 5\n")
   else :
      print("dan bukan bilangan kelipatan 5\n")
else :
   print("Bilangan Ganjil")

# BERBEDA DENGAN SYNTAX INI
# JIKA BILANGAN YANG DIMASUKKAN MERUPAKAN GANJIL MAKA DIA AKAN MENJALANKAN ==BLOK SYNTAX GANJIL==

num = int(input("Masukkan Bilangannyaa: "))

if num % 2 == 0 :
   print("Bilangan Genap")
   if num % 5 == 0 :
      print("dan merupakan bilangan kelipatan 5\n")
   else :
      print("dan bukan bilangan kelipatan 5\n")

else :            #    ==BLOK SYNTAX GANJIL==
   print("Bilangan Ganjil")
   if num % 5 == 0 :
      print("dan merupakan bilangan kelipatan 5\n")
   else :
      print("dan bukan bilangan kelipatan 5\n")




