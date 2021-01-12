SELECT * FROM tabel_A 
WHERE kode_pelanggan = 'dqlabcust03' 
UNION 
SELECT * FROM tabel_B 
WHERE kode_pelanggan = 'dqlabcust03';