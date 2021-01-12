# Definisikan class Karyawan (sebagai base class)
class Karyawan: 
    nama_perusahaan = 'ABC' 
    insentif_lembur = 250000
    def __init__(self, nama, usia, pendapatan): 
        self.nama = nama
        self.usia = usia 
        self.pendapatan = pendapatan 
        self.pendapatan_tambahan = 0
    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur 
    def tambahan_proyek(self, insentif_proyek):
        self.pendapatan_tambahan += insentif_proyek 
    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan
# Buat class turunan (sebagai inherit class) dari class karyawan, 
# yaitu class AnalisData
class AnalisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
    # melakukan pemanggilan konstruktur class Karyawan 
        super().__init__(nama, usia, pendapatan)
    # menerapkan polymorphism dengan mendefinisikan kembali fungsi 
    # lembur() pada class AnalisData 
    def lembur(self):
        # pendapatan tambahan pada class AnalisData sebesar
        # 10 % dari pendapatannya.
        self.pendapatan_tambahan += int(self.pendapatan * 0.1)
# Buat objek karyawan yang bekerja sebagai AnalisData
aksara = AnalisData('Aksara', 25, 8500000)
aksara.lembur()
print(aksara.total_pendapatan())