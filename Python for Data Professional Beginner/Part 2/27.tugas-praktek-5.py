# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]
# Fungsi rata-rata data
def hitung_rata_rata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rata_rata = jumlah/len(data)
    return rata_rata
# Definisikan fungsi hitung_standar_deviasi
def hitung_standar_deviasi(data):
    rata_rata_data = hitung_rata_rata(data)
    varians = 0
    for item in data:
        varians += (item - rata_rata_data) ** 2
    varians /= len(data)
    standar_deviasi = varians ** (1/2)
    return standar_deviasi
# Hitung nilai standar deviasi dari kedua data yang dimiliki
print('Standar deviasi data1:')
print(hitung_standar_deviasi(data1))
print('Standar deviasi data2:')
print(hitung_standar_deviasi(data2))