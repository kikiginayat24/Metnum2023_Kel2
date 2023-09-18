# No 2
# 1. Buatlah modifikasi fungsi ketika kriteria program berhenti adalah sudah mencapai pada iterasi ke-n
# 2. Buatlah modifikasi agar user dapat menginputkan fungsi maupun batas akar dan galatnya
# 3. Buatlah modifikasi agar akarnya dapat ditampilkan dalam bentuk grafik

import numpy as np
import matplotlib.pyplot as plt

# Modifikasi metode bagi dua
def modif_bagidua(f, a, b, tol, n_iterasi):
    nilai_x = [] #Menyimpan nilai x pada setiap iterasi

    #Mengecek apakah f(a) * f(b) >= 0?
    if f(a) * f(b) >= 0:
        print("Tidak terdapat perpotongan akar pada interval ini.")
        return None

    #Tahapan iterasi
    for i in range(1, n_iterasi + 1):
        c = (a + b) / 2.0
        nilai_x.append(c)

        if f(c) == 0 or (b-a) / 2.0 < tol:
            return c, nilai_x

        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2.0, nilai_x

#Inputan dari pengguna untuk fungsi, nilai interval, toleransi, dan jumlah iterasi ke-n
fungsi = input("Inputkan fungsi f(x) : ")
interval_a = float(input("Inputkan batas bawah (a) : "))
interval_b = float(input("Inputkan batas atas (b)  : "))
toleransi = float(input("Inputkan toleransi       : "))
iterasi_ke_n = int(input("Inputkan jumlah maksimal iterasi : "))

#Pendefinisian fungsi dari inputan pengguna/user
def f(x):
    return eval(fungsi)

#Menjalakan metode bagi dua yang telah dimodifikasi
akar, nilai_x = modif_bagidua(f, interval_a, interval_b, toleransi, iterasi_ke_n)
print("Akar : ", akar)

#Data untuk grafik
x = np.linspace(interval_a, interval_b, 100)
y = [f(x_val) for x_val in x]

#Menampilkan grafik fungsi dan titik-titik iterasi
plt.plot(x, y, label=fungsi)
plt.scatter(nilai_x, [f(x_val) for x_val in nilai_x], c='red', label='Iterasi', marker='o')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(akar, color='green', linestyle='--', label='Akar')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.title('Grafik Fungsi dan Titik Iterasi Hasil Metode Bagi Dua')
plt.grid()
plt.show()


