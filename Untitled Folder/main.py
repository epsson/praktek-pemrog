# main.py

# Mengimpor modul-modul yang telah dibuat
import aritmatika
import konversi
import ubah_bilangan

def main_menu():
    """
    Menampilkan menu utama program dan memproses pilihan pengguna.
    Fungsi ini akan terus berjalan hingga pengguna memilih untuk keluar dari program.
    """
    while True:
        print("\n--- Menu Utama ---")
        print("1. Aritmatika")
        print("2. Konversi")
        print("3. Ubah Bilangan")
        print("4. Keluar")

        choice = input("Pilih opsi (1-4): ")

        if choice == '1':
            # Memanggil fungsi menu dari modul aritmatika
            aritmatika.aritmatika_menu()
        elif choice == '2':
            # Memanggil fungsi menu dari modul konversi
            konversi.konversi_menu()
        elif choice == '3':
            # Memanggil fungsi menu dari modul ubah_bilangan
            ubah_bilangan.ubah_bilangan_menu()
        elif choice == '4':
            print("Terima kasih telah menggunakan program ini!")
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    # Memastikan main_menu() hanya dijalankan ketika script dieksekusi langsung
    main_menu()

