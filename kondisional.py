print("======================================")
print("   SISTEM DATA PASIEN RUMAH SAKIT")
print("======================================")

nama = input("Masukkan nama pasien: ")
umur = int(input("Masukkan umur pasien: "))

print("\n===== PILIH JENIS PENYAKIT =====")
print("1. Tifus")
print("2. Tuberkulosis (TBC)")
print("3. Demam Berdarah (DBD)")
print("4. Malaria")
print("5. Diabetes")
print("6. Hipertensi")
print("7. Penyakit Jantung Koroner")
print("8. Stroke")
print("9. Gagal Ginjal")
print("10. Asma")

pilihan = int(input("\nPilih jenis penyakit (1-10): "))

if pilihan == 1:
    penyakit = "Tifus"
    kategori = "Penyakit Infeksi"
    biaya = 350000

elif pilihan == 2:
    penyakit = "Tuberkulosis (TBC)"
    kategori = "Penyakit Infeksi"
    biaya = 400000

elif pilihan == 3:
    penyakit = "Demam Berdarah (DBD)"
    kategori = "Penyakit Infeksi"
    biaya = 450000

elif pilihan == 4:
    penyakit = "Malaria"
    kategori = "Penyakit Infeksi"
    biaya = 400000

elif pilihan == 5:
    penyakit = "Diabetes"
    kategori = "Penyakit Metabolik"
    biaya = 500000

elif pilihan == 6:
    penyakit = "Hipertensi"
    kategori = "Penyakit Kardiovaskular"
    biaya = 400000

elif pilihan == 7:
    penyakit = "Penyakit Jantung Koroner"
    kategori = "Penyakit Kardiovaskular"
    biaya = 800000

elif pilihan == 8:
    penyakit = "Stroke"
    kategori = "Penyakit Neurologis"
    biaya = 750000

elif pilihan == 9:
    penyakit = "Gagal Ginjal"
    kategori = "Penyakit Ginjal"
    biaya = 700000

elif pilihan == 10:
    penyakit = "Asma"
    kategori = "Penyakit Pernapasan"
    biaya = 450000

else:
    penyakit = ""
    kategori = ""
    biaya = 0

if pilihan >= 1 and pilihan <= 10:

    hari = int(input("Berapa hari dirawat: "))

    if hari > 0 and umur > 0:

        total = biaya * hari

        print("\n================================")
        print("       DATA PASIEN OPNAME")
        print("================================")
        print("Nama Pasien    :", nama)
        print("Umur           :", umur, "tahun")
        print("Jenis Penyakit :", penyakit)
        print("Kategori       :", kategori)
        print("Lama Dirawat   :", hari, "hari")
        print("Biaya Per Hari : Rp", biaya)
        print("Total Biaya    : Rp", total)
        print("Status         : Berhasil")
        print("================================")

    else:
        print("Umur atau lama perawatan tidak valid.")

else:
    print("Pilihan penyakit tidak tersedia.")