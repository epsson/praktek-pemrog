import json
from modul.pemilih import PemilihManager
from modul.calon import CalonManager
from modul.voting import VotingSystem
from modul.statistik import Statistik
from modul.utils import clear_screen, pause


def load_data(path):
    with open(path, 'r') as f:
        return json.load(f)


def save_data(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def main():
    clear_screen()
    print("=== Sistem E-Voting Organisasi Mahasiswa ===")

    # Load data
    pemilih_data = load_data('data/pemilih.json')
    calon_data = load_data('data/calon.json')

    pm = PemilihManager(pemilih_data)
    cm = CalonManager(calon_data)
    vs = VotingSystem(pm, cm)
    st = Statistik(pm, cm)

    while True:
        print("\nMenu:")
        print("1. Daftar Pemilih")
        print("2. Daftar Calon")
        print("3. Mulai Voting")
        print("4. Tampilkan Hasil Sementara")
        print("5. Statistik Pemilu")
        print("6. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            pm.tampil_pemilih()
        elif choice == '2':
            cm.tampil_calon()
        elif choice == '3':
            vs.voting()
            save_data('data/pemilih.json', pm.data)
            save_data('data/calon.json', cm.data)
        elif choice == '4':
            cm.tampilkan_hasil()
        elif choice == '5':
            st.tampilkan_statistik()
        elif choice == '6':
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")

        pause()


if __name__ == '__main__':
    main()