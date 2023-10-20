#Interpolasi Polinom dengan Metode Newton

import numpy as np

# Menginput jumlah titik data
n = int(input('Masukkan jumlah titik data: '))

x = np.zeros((n))
y = np.zeros((n,n))

# Memasukkan nilai dari jumlah titik data
print('Masukkan nilai dari titik x dan y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i][0] = float(input( 'y['+str(i)+']='))
    
# Proses Interpolasi Polinom Newton (tabel selisih maju)
for i in range(1,n):
    for j in range(0,n-i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

        
print('\nTabel Selisih Maju Interpolasi Polinom Newton\n');

for i in range(0,n):
    print('%0.2f' %(x[i]), end='')
    for j in range(0, n-i):
        print('\t\t%0.6f' %(y[i][j]), end='')
    print()
