# Latihan tanggal 16 Desember 2020
# Case 1:
# Kita membutuhkan fungsi untuk menghitung jumlah dari list A, kemudian 
# jumlah tersebut ditambahkan kedalam umur kita


def latihan_1 (umur, lists1):
     sum_lists1 = sum(lists1)
     total_lists1_dan_umur = sum_lists1 + umur
     return total_lists1_dan_umur;
    
latihan_umur_lists = latihan_1(30, [10,20,30])
print(latihan_umur_lists)