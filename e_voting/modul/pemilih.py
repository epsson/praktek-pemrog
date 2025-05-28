class PemilihManager:
    def __init__(self, data):
        # data: list of dict {id, nama, jurusan, sudah_memilih}
        self.data = data

    def tampil_pemilih(self):
        print("Daftar Pemilih:")
        for p in self.data:
            status = 'Sudah memilih' if p.get('sudah_memilih', False) else 'Belum memilih'
            print(f"{p['id']} - {p['nama']} ({p['jurusan']}) - {status}")

    def validasi_id(self, pemilih_id):
        for p in self.data:
            if p['id'] == pemilih_id:
                return p
        return None

    def tandai_memilih(self, pemilih_id):
        pemilih = self.validasi_id(pemilih_id)
        if pemilih:
            pemilih['sudah_memilih'] = True
        
    def jumlah_total(self):
        return len(self.data)

    def jumlah_sudah(self):
        return len([p for p in self.data if p.get('sudah_memilih')])