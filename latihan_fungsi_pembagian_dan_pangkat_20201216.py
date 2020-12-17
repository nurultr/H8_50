# Latihan tanggal 16 Desember 2020
# Case 2:
# Kita membuat dua fungsi, dimana fungsi pertama adalah untuk mengecek apakah 
# angka itu dapat dibagi oleh suatu angka (hasilnya true atau false)

angka_1 = 15
angka_2 = 6
angka_3 = 2

def pembagian_dua_angka(angka_1,angka_2):
    if angka_1 % angka_2 ==0:
        hasil = "TRUE"
    else:
        hasil = "FALSE"
    return hasil;

hasil_bagi = pembagian_dua_angka(angka_1, angka_2)
print(hasil_bagi)

def proses_pangkat(hasil_bagi, angka_1, angka_3):
    if hasil_bagi == "TRUE":
        hasil_pangkat = angka_1 ** angka_3
    else:
        hasil_pangkat = "Angka_1 tidak dapat dibagi dengan Angka_2"
    return hasil_pangkat;

hasil_pemangkatan = proses_pangkat(hasil_bagi, angka_1, angka_3)
print(hasil_pemangkatan)
        



