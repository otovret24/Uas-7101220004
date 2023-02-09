# Input omset dan pengeluaran
omset = int(input("Masukkan omset penjualan: "))
pengeluaran = int(input("Masukkan total pengeluaran: "))

# Hitung keuntungan bersih
keuntungan_bersih = omset - pengeluaran

# Hitung keuntungan masing-masing
ali_keuntungan = keuntungan_bersih * 20 / 100
budi_keuntungan = keuntungan_bersih * 30 / 100
susi_keuntungan = keuntungan_bersih * 50 / 100

# Cetak hasil
print("Keuntungan Ali: ", ali_keuntungan)
print("Keuntungan Budi: ", budi_keuntungan)
print("Keuntungan Susi: ", susi_keuntungan)
