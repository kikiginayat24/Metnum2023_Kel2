# Modul matplotlib digunakan untuk membuat grafik dan visualisasi dalam Python.
import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan fungsi, fungsi f(x) didefinisikan untuk menghitung nilai fungsi yang ingin dicari akarnya
def f(x):
    return x**3 + 4*x**2 - 10

# Implementasi Metode Bagi Dua
# Mencari akar dari fungsi f(x) dalam interval antara x0 dan x1,
# dengan memperhitungkan galat yang diinginkan dan batasan jumlah iterasi maksimal
def bagiDua(x0, x1, galat, iterasi_maksimal):
    i = 1
    x_values = []  # Menyimpan nilai x pada setiap iterasi
    kondisi = True
    while kondisi and i <= iterasi_maksimal:  # Menambahkan batasan iterasi maksimal
        x2 = (x0 + x1) / 2
        x_values.append(x2)  # Menyimpan nilai x2 pada setiap iterasi
        print('Iterasi ke-%d, x2 = %0.6f dan f(x2) = %0.6f' % (i, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        i += 1
        kondisi = abs(f(x2)) > galat

    if i > iterasi_maksimal:
        print('\nIterasi maksimal (%d iterasi) telah tercapai.' % iterasi_maksimal)
        print('\nAkar yang ditemukan adalah: %0.8f' % x2)

    return x_values

# Input dari pengguna
# Program utama dimulai dengan input dari pengguna, termasuk tebakan awal (x0 dan x1), galat yang diinginkan, dan jumlah iterasi maksimal.
x0 = float(input('Masukkan Tebakan Pertama: '))
x1 = float(input('Masukkan Tebakan Kedua: '))
galat = float(input('Toleransi Kesalahan: '))
iterasi_maksimal = int(input('Masukkan jumlah iterasi maksimal: '))

# Proses pengecekan dari nilai tebakan yang telah dimasukkan
# Program melakukan pengecekan awal untuk memastikan bahwa tebakan awal mengandung akar (memiliki tanda berlawanan)
if f(x0) * f(x1) > 0.0:
    print('Tebakan yang dimasukkan tidak memiliki nilai akar.')
    print('Coba lagi dengan nilai tebakan yang berbeda!')
    # Jika tebakan awal valid, maka program memanggil fungsi bagiDua untuk mencari akar menggunakan metode bagi dua.
    # Hasil pencarian akar dan iterasi akan dicetak ke layar
else:
    x_values = bagiDua(x0, x1, galat, iterasi_maksimal)

    # Menampilkan grafik fungsi dan akar yang ditemukan
    plt.plot(x_range, y_values, label='Fungsi')  # Plot fungsi sebagai garis
    plt.scatter(x_values, [f(x) for x in x_values], color='red', label='Akar yang Ditemukan', marker='o')  # Tandai akar sebagai titik merah
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Garis horizontal di y = 0
    plt.xlabel('x')  # Label sumbu x
    plt.ylabel('f(x)')  # Label sumbu y
    plt.legend()  # Menampilkan legenda dengan label 'Fungsi' dan 'Akar yang Ditemukan'
    plt.title('Grafik Fungsi dan Akar yang Ditemukan')  # Judul grafik
    plt.grid(True)  # Tampilkan grid pada grafik
    plt.show()  # Tampilkan grafik secara keseluruhan

import matplotlib.pyplot as plt
import numpy as np

# Mendefinisikan fungsi, fungsi f(x) didefinisikan untuk menghitung nilai fungsi yang ingin dicari akarnya
def f(x):
    return x**3 + 4*x**2 - 10

# Implementasi Metode Bagi Dua
# Mencari akar dari fungsi f(x) dalam interval antara x0 dan x1,
# dengan memperhitungkan galat yang diinginkan dan batasan jumlah iterasi maksimal
def bagiDua(x0, x1, galat, iterasi_maksimal):
    i = 1
    x_values = []  # Menyimpan nilai x pada setiap iterasi
    kondisi = True
    while kondisi and i <= iterasi_maksimal:  # Menambahkan batasan iterasi maksimal
        x2 = (x0 + x1) / 2
        x_values.append(x2)  # Menyimpan nilai x2 pada setiap iterasi
        print('Iterasi ke-%d, x2 = %0.6f dan f(x2) = %0.6f' % (i, x2, f(x2)))

        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2

        i += 1
        kondisi = abs(f(x2)) > galat

    if i > iterasi_maksimal:
        print('\nIterasi maksimal (%d iterasi) telah tercapai.' % iterasi_maksimal)
        print('\nAkar yang ditemukan adalah: %0.8f' % x2)

    return x_values

# Input dari pengguna
# Program utama dimulai dengan input dari pengguna, termasuk tebakan awal (x0 dan x1), galat yang diinginkan, dan jumlah iterasi maksimal.
x0 = float(input('Masukkan Tebakan Pertama: '))
x1 = float(input('Masukkan Tebakan Kedua: '))
galat = float(input('Toleransi Kesalahan: '))
iterasi_maksimal = int(input('Masukkan jumlah iterasi maksimal: '))

# Proses pengecekan dari nilai tebakan yang telah dimasukkan
# Program melakukan pengecekan awal untuk memastikan bahwa tebakan awal mengandung akar (memiliki tanda berlawanan)
if f(x0) * f(x1) > 0.0:
    print('Tebakan yang dimasukkan tidak memiliki nilai akar.')
    print('Coba lagi dengan nilai tebakan yang berbeda!')
    # Jika tebakan awal valid, maka program memanggil fungsi bagiDua untuk mencari akar menggunakan metode bagi dua.
    # Hasil pencarian akar dan iterasi akan dicetak ke layar
else:
    x_values = bagiDua(x0, x1, galat, iterasi_maksimal)

    # Menampilkan grafik fungsi dan akar yang ditemukan
    plt.plot(x_range, y_values, label='Fungsi')  # Plot fungsi sebagai garis
    plt.scatter(x_values, [f(x) for x in x_values], color='red', label='Akar yang Ditemukan', marker='o')  # Tandai akar sebagai titik merah
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)  # Garis horizontal di y = 0
    plt.xlabel('x')  # Label sumbu x
    plt.ylabel('f(x)')  # Label sumbu y
    plt.legend()  # Menampilkan legenda dengan label 'Fungsi' dan 'Akar yang Ditemukan'
    plt.title('Grafik Fungsi dan Akar yang Ditemukan')  # Judul grafik
    plt.grid(True)  # Tampilkan grid pada grafik
    plt.show()  # Tampilkan grafik secara keseluruhan
