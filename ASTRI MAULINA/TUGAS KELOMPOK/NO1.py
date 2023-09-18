# Mendefinisikan fungsi f(x) yang akan dicari akarnya.
def f(x):
    return x**3 - 2*x + 1

# Metode Bagi Dua (Bisection Method) untuk mencari akar fungsi.
def metode_bagi_dua(a, b, galat, iterasi_maksimal):
    i = 1
    while i <= iterasi_maksimal:
        c = (a + b) / 2  # Menghitung titik tengah interval
        if f(c) == 0 or (b - a) / 2 < galat:
            return c  # Akar ditemukan atau galat sudah cukup kecil
        i += 1
        if f(c) * f(a) < 0:
            b = c  # Memperbarui batas atas interval
        else:
            a = c  # Memperbarui batas bawah interval
    return None  # Akar tidak ditemukan dalam iterasi maksimal yang ditentukan

# Input dari pengguna untuk interval pencarian dan toleransi galat.
a = float(input('Masukkan batas bawah interval pencarian: '))
b = float(input('Masukkan batas atas interval pencarian: '))
galat = float(input('Masukkan toleransi galat: '))
iterasi_maksimal = int(input('Masukkan jumlah iterasi maksimal: '))

# Memanggil metode bagi dua untuk mencari akar.
akar = metode_bagi_dua(a, b, galat, iterasi_maksimal)

# Menampilkan hasil
if akar is not None:
    print(f'Akar yang ditemukan adalah: {akar:.8f}')
else:
    print('Akar tidak ditemukan dalam jumlah iterasi maksimal yang ditentukan.')

