import numpy as np

#Pendefinisian dengan metode bagi dua
def bagidua(f, a, b, toleransi):

#Mengecek apakah f(a) * f(b) >= 0?
    if f(a) * f(b) >= 0:
    #Jika iya maka tidak ada akar dalam interval tersebut
        print("Tidak terdapat perpotongan akar pada interval ini.")
        return None

    while (b - a) / 2.0 > toleransi:
        #Menghitung nilai tengah interval
        c = (a + b) / 2.0

        #Mengecek apakah akar ditemukan
        if f(c) == 0:
          return c

        #Jika hasil dari f(a) * f(c) < 0, maka batas atas diganti (b = c)
        elif f(a) * f(c) < 0:
            b = c
        #Jika hasil dari f(a) * f(c) > 0, maka batas bawah diganti (a = c)
        else:
            a = c

            return (a+b)/2.0

# Fungsi Pertama
def f1(x):
    return x**3 - 2*x + 1

#Memanggil fungsi metode bagi dua dan menentukan interval
akar1 = bagidua(f1, -2, 2, 0.0001)
print("Akar dari f(x) = x^3 - 2x + 1 adalah :", akar1)

# Fungsi Kedua
def f2(x):
    return np.exp(x) + x

#Memanggil fungsi metode bagi dua dan menentukan interval
akar2 = bagidua(f2, -1, 1, 0.0001)
print("Akar dari f(x) = x^3 - 2x + 1 adalah :", akar2)

