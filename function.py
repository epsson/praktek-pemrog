# 1. Mereverse setiap kata dalam kalimat
def reverse_per_kata(kalimat):
    # Membalik urutan karakter pada setiap kata dalam sebuah kalimat.
    kata2 = kalimat.split()  # Memecah kalimat menjadi list kata-kata berdasarkan spasi
    # Menggunakan list comprehension untuk membalik setiap kata
    # kata[::-1] adalah slicing yang menghasilkan versi terbalik dari string 'kata'
    dibalik = [kata[::-1] for kata in kata2]
    # Menggabungkan kembali list kata-kata yang sudah dibalik menjadi satu string,
    # dipisahkan oleh spasi
    return ' '.join(dibalik)


# 2. Mengurutkan kata berdasarkan indeks list
def urutkan_kalimat(kalimat, urutan):
   
    # Mengurutkan kata-kata dalam sebuah kalimat
    kata2 = kalimat.split()  # Memecah kalimat menjadi list kata-kata

    # Membuat list baru 'hasil' dengan mengambil kata dari 'kata2'
    # Karena 'urutan' adalah 1-based dan list Python 0-based, kita gunakan i-1
    hasil = [kata2[i - 1] for i in urutan]
    # Menggabungkan list kata yang sudah diurutkan menjadi satu string,
    # dipisahkan oleh spasi
    return ' '.join(hasil)

# 3. Mengganti huruf vokal dengan simbol tertentu
def ganti_vokal(kalimat, opsi):

    # Mengganti huruf vokal dalam kalimat dengan simbol tertentu.
    # Pemetaan vokal huruf kecil ke simbol
    vokal_map_kecil = {'a': '4', 'i': '1', 'u': '|_|', 'e': '3', 'o': '0'}
    # Pemetaan vokal huruf besar ke simbol
    vokal_map_besar = {'A': '4', 'I': '1', 'U': '|_|', 'E': '3', 'O': '0'}

    hasil = ""  # String untuk menyimpan hasil akhir
    for huruf in kalimat:  # Iterasi melalui setiap karakter dalam kalimat
        # Jika opsi adalah 1 (untuk vokal kecil)
        if opsi == 1 and huruf in vokal_map_kecil:
            hasil += vokal_map_kecil[huruf]  # Ganti dengan simbol dari map kecil
        # Jika opsi adalah 2 (untuk vokal besar) dan huruf adalah vokal besar
        elif opsi == 2 and huruf in vokal_map_besar:
            hasil += vokal_map_besar[huruf]  # Ganti dengan simbol dari map besar
        else:
            hasil += huruf  # Jika bukan vokal yang dituju atau bukan vokal
    return hasil


# Contoh pemanggilan fungsi
print(reverse_per_kata("AKU CINTA KAMU"))
print(urutkan_kalimat("HARI INI SEDANG BELAJAR PYTHON", [5, 1, 4, 3, 2]))
print(ganti_vokal("Aku Cinta Kamu", 1))
print(ganti_vokal("Aku Cinta Kamu", 2))