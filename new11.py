# Input gaji dan hutang
gaji = int(input("Masukkan gaji: "))
hutang = int(input("Masukkan jumlah hutang: "))

# Hitung sisa gaji setelah dibayar hutang
sisa_gaji = gaji - hutang

# Hitung pemakaian biaya sehari-hari
biaya_sehari_hari = sisa_gaji * 70 / 100

# Hitung jumlah tabungan
tabungan = sisa_gaji * 20 / 100

# Hitung jumlah infak
infak = sisa_gaji - biaya_sehari_hari - tabungan

# Cetak hasil
print("Biaya sehari-hari: ", biaya_sehari_hari)
print("Tabungan: ", tabungan)
print("Infak: ", infak)
