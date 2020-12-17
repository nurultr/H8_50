
# Latihan tanggal 16 Desember 2020
# Latihan fungsi
# Case 3:
# Membuat modul
# Menghitung jumlah data yang ada dalam suatu list
# Masing-masing elemen di list tersebut dikalikan dengan banyaknya data dalam list
# Kemudian jumlahkan semua elemen list tersebut

def hitung_jumlah_data(data_list):
    n = len(data_list)
    return n;

def kali_n_dan_list(data_list, n_data):
    list_baru = []
    for i in range (n_data):
        list_baru.append(n_data * data_list[i])
    return list_baru;

def jumlah_data_baru(list_data_baru):
    total_list_baru = sum(list_data_baru)
    return total_list_baru;
    
        
        




        
