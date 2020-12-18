
# Sesi 4, 17 Desember 2020
# Belajar numpy

namadepan = "nurul"
dim1 = len(namadepan)
namatengah = "tyas"
dim2 = len(namatengah)
namabelakang = "rahmadani"
step_arr = len(namabelakang)


import numpy as np
array1 = np.arange(0,step_arr*dim2,step_arr)
array_nama = np.array([])
for i in range (dim1):
    array_nama = np.append(array_nama,array1)

print(array_nama)



