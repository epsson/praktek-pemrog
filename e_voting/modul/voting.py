class VotingSystem:
    def __init__(self, pemilih_manager, calon_manager):
        self.pm = pemilih_manager
        self.cm = calon_manager

    def voting(self):
        pid = input("Masukkan ID Pemilih: ")
        pemilih = self.pm.validasi_id(pid)
        if not pemilih:
            print("ID Pemilih tidak ditemukan.")
            return
        if pemilih.get('sudah_memilih'):
            print("Pemilih sudah menggunakan hak pilih.")
            return

        cid = input("Masukkan ID Calon yang dipilih: ")
        calon = self.cm.validasi_id(cid)
        if not calon:
            print("ID Calon tidak ditemukan.")
            return

        # Proses pemberian suara
        self.cm.tambah_suara(cid)
        self.pm.tandai_memilih(pid)
        print(f"Terima kasih, {pemilih['nama']}, suara Anda sudah tercatat.")