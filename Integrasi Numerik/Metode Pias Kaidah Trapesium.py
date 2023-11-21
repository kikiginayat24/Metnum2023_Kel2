def trapezoidal_rule(a, b, f, h):
    n = int((b-a)/h)
    fi = 0
    for i in range(n+1):
        print(f"ITERASI KE {i}")
        xi = a + i*h
        if i==0 or i==n:
            print(f"x{i} = {xi}")
            print (f"f({xi}) = {user_function(xi)}")
            fi += user_function(xi)
        else :
            print(f"x{i} = {xi}")
            print (f"f({xi}) = {user_function(xi)}")
            fi += (user_function(xi))*2
    result = h*fi/2
    return result

# Fungsi yang akan diintegrasikan
def user_function(x):
    return 1/(1+x)  # Ganti dengan fungsi yang diinginkan

# Input dari pengguna
a = float(input("Masukkan batas bawah (a): "))
b = float(input("Masukkan batas atas (b): "))
h = float(input("Masukkan panjang langkah (h): "))

# Memanggil fungsi trapezoidal_rule
result = trapezoidal_rule(a, b, f, h)

# Menampilkan hasil
print(f"Hasil integrasi menggunakan metode trapesium: {result}")
