#Mengimport library numpy asa np
import numpy as np

#Fungsi untuk menghitung turunan selisih maju
def selisih_maju(f, x, h):
    turunan = (f(x + h) - f(x)) / h
    return turunan

#Fungsi untuk menghitung turunan selisih mundur
def selisih_mundur(f, x, h):
    turunan = (f(x) - f(x - h)) / h
    return turunan

#Fungsi untuk menghitung turunan selisih tengah
def selisih_tengah(f, x, h):
    turunan = (f(x + h) - f(x - h)) / (2 * h)
    return turunan

#Menginput nilai fungsi
nilai_fungsi = input("Masukkan fungsi : ")
fungsi = lambda x: eval(nilai_fungsi)

#Menginput nilai x
nilai_x = input("Masukkan nilai x : ")
x_array = np.array([float(x) for x in nilai_x.split(',')])

#Menginput nilai h
nilai_h = float(input("Masukkan jarah dari nilai x: "))

#Menghitung nilai turunan selisih maju, mundur, dan tengah
selisih_maju_array = np.vectorize(lambda x: selisih_maju(fungsi, x, nilai_h))(x_array[1:])  
selisih_mundur_array = np.vectorize(lambda x: selisih_mundur(fungsi, x, nilai_h))(x_array[:-1]) 
selisih_tengah_array = np.vectorize(lambda x: selisih_tengah(fungsi, x, nilai_h))(x_array[1:-1]) 

#Memunculkan nilai hasil turunan pertama
print(f"\nFungsi: {nilai_fungsi}")
print(f"Nilai x: {x_array}")
print(f"Nilai h: {nilai_h}")
print("\nTurunan Pertama (Maju):", selisih_maju_array)
print("Turunan Pertama (Mundur):", selisih_mundur_array)
print("Turunan Pertama (Tengah):", selisih_tengah_array)


