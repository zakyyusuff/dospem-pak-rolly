from time import sleep

dpus = "1194069 Zaky Muhammad Yusuf"

# print("This is my file to demonstrate best practices.")

def proses_data(data):
    print("data sedang di proses...")
    ubah_data = data + " telah dimodifikasi"
    sleep(3)
    print("proses ubah Data selesai.")
    return ubah_data