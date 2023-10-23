import numpy as np  # import library numpy alias np

"""
Mendefinisikan fungsi bisection yang akan menghitung akar dengan interval [a,b] dengan toleransi e dengan metode bagi dua
"""
def bisection(f, a, b, e): 
    if np.sign(f(a)) == np.sign(f(b)): 
        raise Exception('Tidak ada akar') 
        # syntax ini berfungsi untuk memberikan pesan jika a dan b sama maka tidak ada akar pada interval tersebut

    c = (a + b) / 2  # Menghitung titik tengah interval [a, b].

    if np.abs(f(c)) < e:
        return c  # kondisi ini berfungsi jika titik berada kurang dari e maka akarnya sudah ditemukan

    elif np.sign(f(a)) == np.sign(f(c)):
        return bisection(f, c, b, e)  # Jika tanda fungsi di a dan c sama, cari akar dalam interval [c, b].

    elif np.sign(f(b)) == np.sign(f(c)):
        return bisection(f, a, c, e)  # Jika tanda fungsi di b dan c sama, cari akar dalam interval [a, c].

# Fungsi pertama : f(x) = x^3 - 2x + 1
f1 = lambda x: x**3 - 2*x + 1

# Mencari akar dari fungsi dalam interval [-1, 2] dengan toleransi 0.1
r1 = bisection(f1, -1, 2, 0.1)
print("r1 =", r1)
print("f1(r1) =", f1(r1))

# Fungsi kedua: f(x) = e^x - x
f2 = lambda x: np.exp(x) - x

# Mencari akar f2 dalam interval [0, 2] dengan toleransi 0.5
r2 = bisection(f2, 0, 2, 0.5)
print("r2 =", r2)
print("f2(r2) =", f2(r2))
