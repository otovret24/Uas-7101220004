# Input nilai
kehadiran = int(input("Masukkan nilai kehadiran (0-100): "))
tugas = int(input("Masukkan nilai tugas (0-100): "))
uts = int(input("Masukkan nilai UTS (0-100): "))
uas = int(input("Masukkan nilai UAS (0-100): "))

# Hitung nilai akhir
na = (kehadiran * 10 / 100) + (tugas * 20 / 100) + (uts * 30 / 100) + (uas * 40 / 100)

# Tentukan grade
if na >= 80:
    grade = "A"
elif na >= 70:
    grade = "B"
elif na >= 60:
    grade = "C"
elif na >= 50:
    grade = "D"
else:
    grade = "E"

# Cetak hasil
print("Nilai akhir: ", na)
print("Grade: ", grade)
