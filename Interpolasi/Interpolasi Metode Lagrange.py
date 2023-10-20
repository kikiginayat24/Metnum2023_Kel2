# Interpolasi Polinom dengan Metode Lagrange

import numpy as np

# Menginput jumlah titik data
n = int(input('Masukkan jumlah titik data: '))

x = np.zeros((n))
y = np.zeros((n))

# Memasukkan nilai dari jumlah titik data
print('Masukkan nilai dari titik x dan y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


# Menentukan nilai titik interpolasi
xp = float(input('Tentukan nilai titik interpolasi: '))

yp = 0

# Proses Interpolasi Polinom Lagrange
for i in range(n):
    
    p = 1
    
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    
    yp = yp + p * y[i]    

# Hasil Interpolasi
print('Nilai titik interpolasi pada %.3f adalah %.3f.' % (xp, yp))
