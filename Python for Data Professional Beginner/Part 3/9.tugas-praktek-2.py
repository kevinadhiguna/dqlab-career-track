# Definisikan perusahaan
perusahaan = Perusahaan('ABC', 'Jl. Jendral Sudirman, Blok 11', '(021)95205XX')
# Definisikan nama-nama karyawan
karyawan_1 = Karyawan('Ani', 25, 8500000, 100000)
karyawan_2 = Karyawan('Budi', 28, 12000000, 150000)
karyawan_3 = Karyawan('Cici', 30, 15000000, 200000)
# Aktifkan karyawan di perusahaan ABC
perusahaan.aktifkan_karyawan(karyawan_1) 
perusahaan.aktifkan_karyawan(karyawan_2) 
perusahaan.aktifkan_karyawan(karyawan_3)