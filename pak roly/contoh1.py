# NPM: 1194069
# nama: Zaky Muhammad Yusuf
# kelas: D4 Ti 4B
# dospem: Bpk Rolly Maulana Awangga

# ------------------------------------------------------------------------------------------------------------------
# def Belajar():
#     print("percobaan 1")
#     return Belajar

# Belajar()

# ------------------------------------------------------------------------------------------------------------------

# def nomor():
#     print("0812345678")

# def kalimat():
#     print("haloo saya dari instansi XXXXX silahkan transfer ke rekening berikut")

# def hasil():
#     print("penipuan")

# nomor()
# kalimat()
# hasil()

# -------------------------------------------------------------------------------------------------------------------

# def abc():
#     print("masukan nomor: ")
#     # print("masukan kalimat: ")
#     a = input()
#     print("masukan kalimat: ")
#     b = input()
#     print("nomor yang anda masukan adalah, "+ a)
#     print("kalimat yang anda masukan adalah, "+ b)

#     return a+b
# abc()

# --------------------------------------------------------------------------------------------------------------------

# def abc():
#     nomor = input("masukan nomor: ")
#     kalimat = input("masukan kalimat: ")
#     print(nomor, kalimat)
# abc()

# ---------------------------------------------------------------------------------------------------------------------

# def abc():
#     print("deteksi spam sms")
#     nomor = input("masukan nomor: ")
#     kalimat = input("masukan kalimat: ")
#     print(int(nomor), str(kalimat))
# abc()

# ----------------------------------------------------------------------------------------------------------------------

# print("deteksi spam sms")
# kalimat = str(input('Masukkan kalimat: '))

# if kalimat == ("kehabisan pulsa silahkan beli di konter kami"):
#     print('promosi')
# elif kalimat == ("selamat pagi bapak dosen yang baik hati"):
#     print('normal')
# elif kalimat == ("ayo silahkan bermain di link kami dijamin menang"):
#     print('judi')
# elif kalimat == ("silahkan transfer ke rekening saya"):
#     print('penipuan')
# else:
#     print('coba cek kalimat anda mungkin typo')

# ----------------------------------------------------------------------------------------------------------------------

def sample():
    print("deteksi spam sms")
    nomor = str(input('masukan nomor: '))
    kalimat = str(input('Masukkan kalimat: '))

    if nomor+kalimat == ("123" "kehabisan pulsa silahkan beli di konter kami"):
        print('promosi')
    elif nomor+kalimat == ("456" "selamat pagi bapak dosen yang baik hati"):
        print('normal')
    elif nomor+kalimat == ("789" "ayo silahkan bermain di link kami dijamin menang"):
        print('judi')
    elif nomor+kalimat == ("021" "silahkan transfer ke rekening saya"):
        print('penipuan')
    else:
        print('coba cek nomor atau kalimat mungkin typo')

sample()