
from time import sleep

dpus = "1194069 Zaky Muhammad Yusuf"

def test_proses_data():
    data = dpus
    print("data sedang di proses...")
    ubah_data = data + " telah dimodifikasi"
    sleep(3)
    print("proses ubah Data selesai.")
    assert ubah_data


# pytest pusat.py