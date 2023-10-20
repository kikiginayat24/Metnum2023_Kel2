# Import library NumPy untuk manipulasi matriks
import numpy as np

# Fungsi dekomposisi LU
def dekomposisi_LU(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    # Iterasi untuk mengisi matriks L dan U
    for k in range(n):
        L[k, k] = 1
        for i in range(k, n):
            U[k, i] = A[k, i]
            for j in range(k):
                U[k, i] -= L[k, j] * U[j, i]

        for i in range(k + 1, n):
            L[i, k] = A[i, k]
            for j in range(k):
                L[i, k] -= L[i, j] * U[j, k]
            L[i, k] /= U[k, k]

    return L, U

# Fungsi substitusi maju
def forward_substitution(L, b):
    n = len(b)
    y = np.zeros(n)

    # Iterasi untuk menghitung nilai y
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i, j] * y[j]
        y[i] /= L[i, i]

    return y

# Fungsi substitusi mundur
def backward_substitution(U, y):
    n = len(y)
    x = np.zeros(n)

    # Iterasi untuk menghitung nilai x
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i, j] * x[j]
        x[i] /= U[i, i]

    return x

# Contoh penggunaan
A = np.array([[2, -1, 1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

# Memanggil fungsi dekomposisi_LU
L, U = dekomposisi_LU(A)

# Memanggil fungsi substitusi maju dan mundur
y = forward_substitution(L, b)
x = backward_substitution(U, y)

# Menampilkan hasil
print("Matrix L:")
print(L)
print("\nMatrix U:")
print(U)
print("\nNilai y:")
print(y)
print("\nNilai x:")
print(x)
