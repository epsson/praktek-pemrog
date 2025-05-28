# aritmatika.py

def penjumlahan(a, b):
    """
    Menghitung penjumlahan dua bilangan.
    Args:
        a (float): Bilangan pertama.
        b (float): Bilangan kedua.
    Returns:
        float: Hasil penjumlahan.
    """
    return a + b

def perpangkatan(a, b):
    """
    Menghitung perpangkatan (a^b) dua bilangan.
    Args:
        a (float): Bilangan dasar.
        b (float): Pangkat.
    Returns:
        float: Hasil perpangkatan.
    """
    return a ** b

def perkalian(a, b):
    """
    Menghitung perkalian dua bilangan.
    Args:
        a (float): Bilangan pertama.
        b (float): Bilangan kedua.
    Returns:
        float: Hasil perkalian.
    """
    return a * b

def aritmatika_menu():
    """
    Menampilkan sub-menu aritmatika dan memproses pilihan pengguna.
    Fungsi ini akan terus berjalan hingga pengguna memilih untuk kembali ke menu utama.
    """
    while True:
        print("\n--- Sub-menu Aritmatika ---")
        print("1. Penjumlahan")
        print("2. Perpangkatan")
        print("3. Perkalian")
        print("4. Kembali ke Menu Utama")

        choice = input("Pilih operasi (1-4): ")

        if choice == '1':
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
                print(f"Hasil Penjumlahan: {penjumlahan(num1, num2)}")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif choice == '2':
            try:
                num1 = float(input("Masukkan angka dasar: "))
                num2 = float(input("Masukkan pangkat: "))
                print(f"Hasil Perpangkatan: {perpangkatan(num1, num2)}")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif choice == '3':
            try:
                num1 = float(input("Masukkan angka pertama: "))
                num2 = float(input("Masukkan angka kedua: "))
                print(f"Hasil Perkalian: {perkalian(num1, num2)}")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
        elif choice == '4':
            break  # Keluar dari sub-menu aritmatika
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

