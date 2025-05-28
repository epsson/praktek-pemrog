# ubah_bilangan.py

def desimal_to_biner(desimal):
    """
    Mengubah bilangan desimal ke biner.
    Args:
        desimal (int): Bilangan desimal.
    Returns:
        str: Representasi biner.
    """
    return bin(desimal).replace("0b", "")

def desimal_to_oktal(desimal):
    """
    Mengubah bilangan desimal ke oktal.
    Args:
        desimal (int): Bilangan desimal.
    Returns:
        str: Representasi oktal.
    """
    return oct(desimal).replace("0o", "")

def desimal_to_heksadesimal(desimal):
    """
    Mengubah bilangan desimal ke heksadesimal.
    Args:
        desimal (int): Bilangan desimal.
    Returns:
        str: Representasi heksadesimal.
    """
    return hex(desimal).replace("0x", "").upper()

def ubah_bilangan_menu():
    """
    Menampilkan sub-menu ubah bilangan dan memproses pilihan pengguna.
    Fungsi ini akan terus berjalan hingga pengguna memilih untuk kembali ke menu utama.
    """
    while True:
        print("\n--- Sub-menu Ubah Bilangan ---")
        print("1. Desimal ke Biner")
        print("2. Desimal ke Oktal")
        print("3. Desimal ke Heksadesimal")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih konversi (1-4): ")

        if choice == '1':
            try:
                desimal = int(input("Masukkan angka desimal: "))
                print(f"Desimal {desimal} = Biner {desimal_to_biner(desimal)}")
            except ValueError:
                print("Input tidak valid. Harap masukkan bilangan bulat.")
        elif choice == '2':
            try:
                desimal = int(input("Masukkan angka desimal: "))
                print(f"Desimal {desimal} = Oktal {desimal_to_oktal(desimal)}")
            except ValueError:
                print("Input tidak valid. Harap masukkan bilangan bulat.")
        elif choice == '3':
            try:
                desimal = int(input("Masukkan angka desimal: "))
                print(f"Desimal {desimal} = Heksadesimal {desimal_to_heksadesimal(desimal)}")
            except ValueError:
                print("Input tidak valid. Harap masukkan bilangan bulat.")
        elif choice == '4':
            break  # Keluar dari sub-menu ubah bilangan
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

