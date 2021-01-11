list_tagihan = [50000, 75000, -150000, 125000, 300000, -50000, 200000]
total_tagihan = 0
for tagihan in list_tagihan :
    if tagihan < 0 :
        print("terdapat angka minus dalam tagihan, perhitungan dihentikan!")
        break
    total_tagihan += tagihan
print(total_tagihan)