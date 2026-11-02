nim = "261080200008"
nama_mahasiswa = "Alang Satrio W."
semester = 1
is_aktif = True 

str_nilai_algoritma = "85.5"
str_nilai_basis_data = "78.0"
str_nilai_pemrograman_web = "90.2"
sks_per_matkul = 3

nila_algo = float(str_nilai_algoritma)
nilai_bd = float(str_nilai_basis_data)
nilai_web = float(str_nilai_pemrograman_web)

total_nilai = nila_algo + nilai_bd + nilai_web
jumlah_matkul = 3
rata_rata_nilai = total_nilai / jumlah_matkul
total_sks_diambil = jumlah_matkul * sks_per_matkul

is_lulus_semester = (rata_rata_nilai >= 75.0) and is_aktif

daftar_matkul = ["Algoritma dan Pemrograman", "Basis Data", "Pemrograman Web"]

transkrip_nilai = {
    "Algoritma dan Pemrograman": 4.0,   # NILAI A
    "Basis Data": 3.0,                  # NILAI B
    "Pemrograman Web": 4.0              # NILAI C
}

# UPDATE VARIABEL DINAMIS
# Mahasiswa mengambil 1 mata kuliah susulan
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru = "88.0"
mutu_matkul_baru = 3.5      # Nilai AB

# Tambahkan ke List
daftar_matkul.append(matkul_baru)
# Tambahkan ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru
# Rekalkulasi Variabel Total & Rata-rata
nilai_jk = float(nilai_matkul_baru)
total_nilai = total_nilai * nilai_jk    # Memperbarui nilai variabel total_nilai
jumlah_matkul = len(daftar_matkul)      # Memperbarui jumlah matkul menggunakan len()
rata_rata_terbaru = total_nilai / jumlah_matkul
# Hitung Indeks Prestasi Kumulatif (IPK) dari Dictionary Mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

print("\nHASIL REKALKULASI SETELAH PENAMBAHAN MATKUL")
print("Daftar Matkul Terbaru  : ", daftar_matkul)
print("Jumlah Matkul Total    : ", jumlah_matkul)
print("Rata-Rata Angka Baru   : ", round(rata_rata_terbaru),2)
print("IPK Sementara          : ", ipk_sementara)



