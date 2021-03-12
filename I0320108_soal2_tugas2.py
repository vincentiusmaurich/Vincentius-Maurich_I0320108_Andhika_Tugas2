# Input Variabel
nama_lengkap = "Vincentius Maurich Kian Mulya"
nama = "Maurich"
tempat_lahir = "Surakarta"
tanggal_lahir = 7
bulan_lahir = 5
tahun_lahir = 2002
tanggal_now = 12
bulan_now = 3
tahun_now = 2021
tinggi = 165
berat = 50
sepatu = 43
minus = 0.5
alamat = "Pengin, Cangkol, Mojolaban, Sukoharjo"

# Menghitung Umur dalam Bulan
umur_bulan = ((tanggal_now - tanggal_lahir)/30) + (bulan_now - bulan_lahir) + ((tahun_now - tahun_lahir) * 12)

# Menghitung Umur dalam Tahun
umur_tahun = tahun_now - tahun_lahir

# Menampilkan Biodata
print("Biodata Saya")
print("Nama lengkap saya adalah ", nama_lengkap)
print("Saya kerap disapa dengan nama ", nama)
print("Saya lahir di ", tempat_lahir, umur_tahun, "tahun yang lalu, atau tepatnya ", int(umur_bulan), "bulan yang lalu")
print("Secara postur, tinggi badan saya mencapai ", tinggi, "cm dengan berat badan sebesar ", berat, "kg")
print("Sepatu yang cukup untuk kaki saya berukuran ", sepatu)
print("Kedua mata saya masing-masing mengalami miopi atau minus sebesar ", float(minus))
print("Saat ini, saya tinggal di ", alamat)