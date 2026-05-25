mobil_harga = [["Toyota Avanza", 200000000], ["Honda Brio", 150000000], ["Daihatsu Xenia", 180000000], [ "Suzuki Ertiga", 220000000], ["Mitsubishi Xpander", 250000000]]

def menu():
    print("Menu:")
    print("1. Lihat seluruh mobil")
    print("2. Tambah mobil")
    print("3. Hapus mobil")
    print("4. Ubah harga mobil")
    print("5. Keluar")

def lihat_mobil():
    print("\nData Harga Mobil:")

    # jika data kosong
    if not mobil_harga:
        print("Mobil tidak tersedia.")
        return
    
    # menampilkan setiap merek dan harga
    for merek, harga in mobil_harga:
        print(f"- {merek}: Rp {harga},")

def tambah_mobil():
    merek = input("Masukkan merek mobil: ")
    harga = int(input("Masukkan harga mobil: "))
    mobil_harga.append([merek, harga])
    print(f"{merek} berhasil ditambahkan dengan harga Rp {harga}.")

def hapus_mobil():
    merek = input("Masukkan merek mobil yang ingin dihapus: ")
    for i, (m, h) in enumerate(mobil_harga):
        if m.lower() == merek.lower():
            del mobil_harga[i]
            print(f"{merek} berhasil dihapus.")
            return
    print(f"{merek} tidak ditemukan.")

def ubah_harga():
    merek = input("Masukkan merek mobil yang ingin diubah harganya: ")
    for i, (m, h) in enumerate(mobil_harga):
        if m.lower() == merek.lower():
            harga_baru = int(input(f"Masukkan harga baru untuk {merek}: "))
            mobil_harga[i][1] = harga_baru
            print(f"Harga {merek} berhasil diubah menjadi Rp {harga_baru}.")
            return
    print(f"{merek} tidak ditemukan.")

def mobil():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            lihat_mobil()
        elif pilihan == "2":
            tambah_mobil()
        elif pilihan == "3":
            hapus_mobil()
        elif pilihan == "4":
            ubah_harga()
        elif pilihan == "5":
            print("Terima kasih telah mengunjungi toko ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

mobil()