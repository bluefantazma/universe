
def toko():
    
    produk_dict = {
        1: ('apel', 10000),
        2: ('ceri', 6000),
        3: ('melon', 8000)
    }
    
    penjualan = []
    invoice_number = 1

    while True:
        print('Selamat Datang, Admin Penjualan Toko Maju Makmur')
        print('Silakan pilih menu yang anda inginkan : ')
        print("\nMenu:")
        print("1. Input Penjualan")
        print("2. Tampilkan Penjualan")
        print("3. Hapus Penjualan")
        print("4. Edit Penjualan")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == '1':
            print("\nDaftar Produk:\n1.Apel, Harga 10000\n2.Ceri, Harga 6000\n3.Melon, Harga 8000.")
            
            try:
                produk_id = int(input("Masukkan nomor produk: "))
                if produk_id in produk_dict:
                    jumlah = int(input("Masukkan jumlah penjualan: "))
                    nama_produk, harga = produk_dict[produk_id]
                    total_harga = harga * jumlah
                    penjualan.append([invoice_number, nama_produk, harga, jumlah, total_harga])
                    print(f"Penjualan dicatat dengan nomor invoice {invoice_number}")
                    invoice_number += 1
                    print('Terima kasih.')
                    print('='*25)
                else:
                    print("Produk tidak ditemukan.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan nomor yang benar.")

        elif pilihan == '2':
            print('Pilih apakah anda ingin invoice tertentu ataukah seluruh data.\n1.Masukkan Nomor Invoice\n2.Tampilkan semua')
            tampilan = input('masukkan pilihan anda (1/2): ')

            if tampilan == '1':               
                try:
                    tampilan_invoice = int(input('masukkan nomor invoice: '))
                    for item in penjualan:
                        if item[0] == tampilan_invoice:
                            print(f"Invoice: {item[0]}, Produk: {item[1]}, Harga: {item[2]}, Jumlah: {item[3]}, Total Harga: {item[4]}")
                            print('Terima kasih.')
                            print('='*25)
                            break
                    else:
                        print("Input tidak valid.")
                except ValueError:
                    print("Input tidak valid.")

            elif tampilan == '2':
            
                if penjualan:
                    print("\nDaftar Penjualan:")
                    for item in penjualan:
                        print(f"Invoice: {item[0]}, Produk: {item[1]}, Harga: {item[2]}, Jumlah: {item[3]}, Total Harga: {item[4]}")
                        print('Terima kasih.')
                        print('='*25)
                else:
                    print("Belum ada data penjualan.")
            else :
                print("Input tidak valid")


        elif pilihan == '3':
            if penjualan:
                try:
                    hapus_invoice = int(input("Masukkan nomor invoice yang akan dihapus: "))
                    penjualan = [item for item in penjualan if item[0] != hapus_invoice]
                    print(f"Data dengan nomor invoice {hapus_invoice} telah dihapus.")
                    print('Terima kasih.')
                    print('='*25)
                except ValueError:
                    print("Input tidak valid. Silakan masukkan nomor invoice yang benar.")
            else:
                print("Belum ada data penjualan.")

        elif pilihan == '4':
            if penjualan:
                try:
                    edit_invoice = int(input("Masukkan nomor invoice yang akan diubah: "))
                    for item in penjualan:
                        if item[0] == edit_invoice:
                            jumlah_baru = int(input(f"Masukkan jumlah baru untuk produk {item[1]}: "))
                            item[3] = jumlah_baru
                            item[4] = item[2] * jumlah_baru
                            print(f"Data dengan nomor invoice {edit_invoice} telah diperbarui.")
                            print('Terima kasih.')
                            print('='*25)
                            break
                    else:
                        print("Nomor invoice tidak ditemukan.")
                except ValueError:
                    print("Input tidak valid. Silakan masukkan nomor yang benar.")
            else:
                print("Belum ada data penjualan.")

        
        elif pilihan == '5':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")


toko()
print('Terima kasih.')
print('='*25)