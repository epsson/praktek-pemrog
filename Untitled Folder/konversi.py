# konversi.py

def cm_to_m(cm):
    """
    Mengubah panjang dari Centimeter (CM) ke Meter (M).
    Args:
        cm (float): Panjang dalam Centimeter.
    Returns:
        float: Panjang dalam Meter.
    """
    return cm / 100

def m_to_cm(m):
    """
    Mengubah panjang dari Meter (M) ke Centimeter (CM).
    Args:
        m (float): Panjang dalam Meter.
    Returns:
        float: Panjang dalam Centimeter.
    """
    return m * 100

def konversi_menu():
    """
    Menampilkan sub-menu konversi dan memproses pilihan pengguna.
    Fungsi ini akan terus berjalan hingga pengguna memilih untuk kembali ke menu utama.
    """
    while True:
        print("\n--- Sub-menu Konversi ---")
        print("1. CM ke M")
        print("2. M ke CM")
        print("3. Kembali ke Menu Utama")

        choice = input("Pilih konversi (1-3): ")

        if choice == '1':
            try:
                cm = float(input("Masukkan panjang dalam CM: "))
                print(f"{cm} CM = {cm_to_m(cm)} M")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka desimal.")
        elif choice == '2':
            try:
                m = float(input("Masukkan panjang dalam M: "))
                print(f"{m} M = {m_to_cm(m)} CM")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka desimal.")
        elif choice == '3':
            break  # Keluar dari sub-menu konversi
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

