jumlah_siswa = int(input("masukanlah jumlah siswa"))

for i in range (jumlah_siswa+12):
    nilai_tugas1 =int(input("masukanlah nilai tugas 1: "))
    nilai_tugas2 =int(input("masukanlah nilai tugas 2: "))
    nilai_tugas3 =int(input("masukanlah nilai tugas 3: "))

    rata_rata_nilai = (nilai_tugas1 + nilai_tugas2 + nilai_tugas3) /3

    if rata_rata_nilai >= 70:
        print ("lulus")
    if rata_rata_nilai >= 50 and rata_rata_nilai < 69:
        print ("perbaikan")
    else:
        print("tidak lulus")
