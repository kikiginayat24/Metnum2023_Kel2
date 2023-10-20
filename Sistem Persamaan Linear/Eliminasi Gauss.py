def eliminasi_gauss(matriks):
    # Deklarasi fungsi eliminasi gauss, yang akan merima matriks sebagai argumen
    # Fungsi ini akan melakukan langkah-langkah eliminasi gauss pada matriks
    # untuk menyederhanakannya menjadi bentuk segitiga atas
    baris, kolom = len(matriks), len(matriks[0])
    # Menghitung baris dan kolom matriks agar bisa digunakan dalam iterasi
    
    for i in range(baris): # Loop yang akan berjalan sebanyak jumlah baris dalam matriks
        # Membuat elemen diagonal utama menjadi 1
        faktor_skala = 1.0 / matriks[i][i]
        for j in range(kolom):
            matriks[i][j] *= faktor_skala

        # Menghilangkan elemen di bawah diagonal utama
        # Setiap baris bawah akan dikurangi dengan faktor eliminasi dikali elemen utama dibaris saat ini
        for k in range(i + 1, baris):
            faktor_elim = matriks[k][i]
            for j in range(kolom):
                matriks[k][j] -= faktor_elim * matriks[i][j]

def substitusi_mundur(matriks):
  # Deklarasi subsitusi mundur yang menerima matriks setelah eliminasi gauss sebagai argumen
  # yang akan digunakan untuk mencari solusi persamaan linear
    baris, kolom = len(matriks), len(matriks[0])
    solusi = [0] * baris

    for i in range(baris - 1, -1, -1):
        solusi[i] = matriks[i][kolom - 1]
        for j in range(i + 1, baris):
            solusi[i] -= matriks[i][j] * solusi[j]
            # Baris diatas merupakan langkah-langkah subsitusi mundur
            # Setap solusi dihitung dengan mengurangkan produk dari koefisien
            # yang diketahui dan solusi yang sudah diketahui

    return solusi

def tampilkan_matriks(matriks): #  Fungsi ini akan menampilkan matriks
    for baris in matriks:
        print(baris)

# Contoh penggunaan
sistem_persamaan = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3]
]

eliminasi_gauss(sistem_persamaan)
hasil = substitusi_mundur(sistem_persamaan)

print("Matriks setelah eliminasi Gauss:")
tampilkan_matriks(sistem_persamaan)

print("Solusi sistem persamaan:")
print(hasil)
