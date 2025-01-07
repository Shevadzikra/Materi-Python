#CASTING ADALAH MERUBAH TIPE DATA KE TIPE DATA LAIN

dataInt = 5
print(dataInt, type(dataInt))

print("===MERUBAH DATA INTEGER KE STRING===")
dataStr = str(dataInt)
print(dataStr, type(dataStr))

print("===MERUBAH DATA YANG SEMULA STRING KE INT===")
dataMix = int(dataStr)
print(dataMix, type(dataMix))

numberString = 10

print(numberString + dataMix)