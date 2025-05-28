class CalonManager:
    def __init__(self, data):
        # data: list of dict {id, nama, visi, jumlah_suara}
        self.data = data

    def tampil_calon(self):
        print("Daftar Calon Ketua:")
        for c in self.data:
            print(f"{c['id']} - {c['nama']} (Visi: {c['visi']}) - Suara: {c.get('jumlah_suara', 0)}")

    def validasi_id(self, calon_id):
        for c in self.data:
            if c['id'] == calon_id:
                return c
        return None

    def tambah_suara(self, calon_id):
        calon = self.validasi_id(calon_id)
        if calon:
            calon['jumlah_suara'] = calon.get('jumlah_suara', 0) + 1

    def tampilkan_hasil(self):
        print("Hasil Voting Sementara:")
        self.tampil_calon()