anak_anak = 30.000
dewasa = 50.000
lansia = 35.000

total_harga_keseluruhan = 0

jumlah_pembeli = int(input("masukan jumlah pebeli tiket: "))

for i in range(jumlah_pembeli) :
    usia = int(input("masukan usia anda:"))
    jumlah_tiket = int(input("masukan jumlah tiket yang dibeli: "))

    if usia <=12:
        harga_tiket =anak_anak
    elif usia <= 60:
        harga_tiket = dewasa
    else:
        harga_tiket = lansia

    total_harga_pembeli = harga_tiket * jumlah_tiket
    print (f"harga tiket untuk pembeli = {i+1}, dan jumlah total pembelinnya = {total_harga_pembeli}")

    total_harga_keseluruhan = total_harga_keseluruhan + total_harga_pembeli
print (f"total harga tiket keseluruhan = {total_harga_pembeli}")