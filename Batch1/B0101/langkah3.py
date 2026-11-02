# LIST (Berurutan, bisa diubah)
hobi = ["Membaca", "Koding", "Berenang"]
print("List Hobi : ", hobi)
print("Tipe Data : ", type(hobi))

# TUPLE (Berurutan, TIDAK BISA diubah)
koordinat = (-6.171, 106.8650)
print("Tuple Koordinat : ", koordinat)
print("Tipe Data : ", type(koordinat))

# DICTIONARY (Pasangan Key : Value)
mahasiswa = {
    "nama": "Alang",
    "nim": "008",
    "ipk": 3.85
}
print("Dict Mahasiswa : ", mahasiswa)
print("Nama Mahasiswa : ", mahasiswa["nama"])
print("Tipe : ", type(mahasiswa))

# SET (Nilai unik, tidak berurutan, tidak dapat diduplikat)
angka_unik = {1,2,2,3,4,4,5}
print("Set Angka Unit (otomatis menghapus duplikat) : ", angka_unik)
print("Tipe : ", type(angka_unik))