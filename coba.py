import requests as re
import config

def kirim():
    pesan = input("Masukkan Pesan yang dikirim: ")
    jumlah = int(input("Masukkan Jumlah Pesan : "))
    for i in range(1, jumlah):
        re.post(f'https://api.telegram.org/bot{config.bot_token}/sendMessage?chat_id={config.chat_id}&text={pesan}')
        print(f"Berhasil Kirim No{i}")

try:
    kirim()
except ValueError:
    print("Jumlahnya Spamnya Berapa Bujang???????")
    print("="*20)
    print("Ulangi Lagi")
    kirim()