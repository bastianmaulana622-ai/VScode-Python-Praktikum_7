# Program 9.1: Pembuatan List

# Kumpulan data numbers
data_angka = [1, 5, 2, 3]
print(data_angka)

# Kumpulan data string
data_string = ["ucup", "adit", "siti"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, True]
print(data_boolean)

# Kumpulan campuran
data_campuran = [1, "bakwan", 2, "cireng", "ucup", True, "adit", False]
print(data_campuran)

## Cara alternatif membuat list
data_range = range(0, 10, 2)  # range(start, stop, step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop (list comprehension)
list_for = [i * 2 for i in range(0, 10)]
print(list_for)

# Membuat list dengan for dan if
list_for_if = [i for i in range(0, 10) if i != 5]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0, 10) if i % 2 != 0]
print(list_for_if)

# Program 9.2: Manipulasi List

data = ["Ucup", "Adit", "Dudung"]

# Mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")
data_terakhir = data[-1]
print(f"data terakhir adalah = {data_terakhir}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# Manipulasi data list
print(f"data sebelum ditambah = \n{data}")
data.insert(1, "Asep")
print(f"data sesudah ditambah = \n{data}")

# Menambah di akhir list
data.append("Ririn")
print(f"data ditambah lagi = \n{data}")

# Menambahkan list dengan list
data_baru = ["Luffy", "Zoro", "Nami"]
data.extend(data_baru)
print(f"data gabungan = \n{data}")

# Mengubah data (merubah data indeks 2 menjadi jarwo)
data[2] = "jarwo"
print(f"data rubah = \n{data}")

# Menghapus data berdasarkan nama
data.remove("Ucup")
print(f"data hapus = \n{data}")

# Menghapus data paling belakang
data.pop()
print(f"data akhir = \n{data}")

# Program 9.3: Operasi List

data_angka = [1, 5, 1, 4, 3, 2, 4, 3, 2, 3, 7, 8, 9, 0]
print(f"data angka = \n{data_angka}")

# Count data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print(f"jumlah angka 4 = {jumlah_data_4}")
print(f"jumlah angka 3 = {jumlah_data_3}")

# Ambil posisi data
data = ["Rendi", "Iqbal", "Gana", "Khairil"]
print(f"data = {data}")

index_Iqbal = data.index("Iqbal")
index_Gana = data.index("Gana")
print(f"index si Iqbal = {index_Iqbal}")
print(f"index si Gana = {index_Gana}")

# Mengurutkan list
print(f"data angka sebelum sort = \n{data_angka}")
data_angka.sort()
print(f"data angka sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# Balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse \n{data_angka}")
print(f"data di reverse \n{data}")

# Program 9.4: Nested List

data_0 = [1, 2]
data_1 = [3, 4]
data_list_biasa = [1, 2, 3, 4]
print(f"list biasa {data_list_biasa}")

list_2D = [data_0, data_1, 6, 7]
print(f"list 2D {list_2D}")

# Contoh penggunaan
peserta_0 = ["Rendi", 25, "Laki-laki"]
peserta_1 = ["Joni", 10, "Laki-laki"]
peserta_2 = ["Eka", 50, "Wanita"]

list_peserta = [peserta_0, peserta_1, peserta_2]
print(f"peserta = {list_peserta}\n")

for peserta in list_peserta:
    print(f"nama\t: {peserta[0]}")
    print(f"umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")



# IV. LATIHAN SOAL MODUL

# Latihan 1

# Kode Program:

kendaraan = ['motor', 'mobil', 'sepeda', 'bus']

# a. Tambahkan 'truk' di akhir list
kendaraan.append('truk')

# b. Sisipkan 'becak' pada index ke-1
kendaraan.insert(1, 'becak')

# c. Hapus data paling belakang
kendaraan.pop()

# d. Ubah 'sepeda' menjadi 'skuter'
index_sepeda = kendaraan.index('sepeda')
kendaraan[index_sepeda] = 'skuter'

# e. Tampilkan jumlah total data
total_data = len(kendaraan)

print(f"Hasil akhir list kendaraan: {kendaraan}")
print(f"Jumlah total data: {total_data}")


# Latihan 2

# Kode Program:

angka = [75, 80, 90, 75, 85, 100, 65]

# a. Indeks skor 100
index_100 = angka.index(100)
print(f"Skor 100 berada pada indeks ke-: {index_100}")

# b. Banyak siswa mendapat skor 75
jumlah_75 = angka.count(75)
print(f"Banyak siswa yang mendapat skor 75: {jumlah_75}")

# c. Urutkan dari terkecil ke terbesar
angka.sort()
print(f"Urutan terkecil ke terbesar: {angka}")

# d. Balikkan urutan dari terbesar ke terkecil
angka.reverse()
print(f"Urutan terbesar ke terkecil: {angka}")


# Latihan 3

# Kode Program:

menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]

# Menggabungkan menu_tambahan ke menu_utama menggunakan fungsi extend
menu_utama.extend(menu_tambahan)

print(f"Hasil gabungan menu: {menu_utama}")


# Latihan 4

# Kode Program:

data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Akses harga "Pensil" (Baris 1, Kolom 1)
harga_pensil = data_barang[1][1]
print(f"Harga Pensil (akses indeks [1][1]): {harga_pensil}")
print("-" * 35)

# b. Membaca data dengan perulangan
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")
