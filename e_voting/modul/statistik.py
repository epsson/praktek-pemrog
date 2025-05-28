class Statistik:
    def __init__(self, pemilih_manager, calon_manager):
        self.pm = pemilih_manager
        self.cm = calon_manager

    def tampilkan_statistik(self):
        total = self.pm.jumlah_total()
        sudah = self.pm.jumlah_sudah()
        partisipasi = (sudah / total * 100) if total > 0 else 0

        print("Statistik Pemilu:")
        print(f"Total pemilih      : {total}")
        print(f"Sudah memilih      : {sudah}")
        print(f"Partisipasi       : {partisipasi:.2f}%")

        # Calon dengan suara terbanyak
        suara_max = max(self.cm.data, key=lambda c: c.get('jumlah_suara', 0))
        print(f"Pemimpin sementara : {suara_max['nama']} ({suara_max.get('jumlah_suara', 0)} suara)")