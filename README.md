# Hiyrid Bot

Hiyrid Bot adalah bot Telegram sederhana yang dibuat menggunakan Python dan library python-telegram-bot. 
Bot ini dirancang untuk berinteraksi dengan pengguna, merespons perintah dasar seperti "/**start**" dan "/**help**", serta mengulang pesan yang dikirim oleh pengguna.

## Fitur

  1. **Start Command**: Mengirim pesan sambutan ketika perintah /start digunakan.
  2. **Help Command**: Menyediakan informasi bantuan dengan perintah /help.
  3. **Echo**: Mengulang pesan teks yang dikirim oleh pengguna.

## Prasyarat
  
Sebelum menjalankan bot, pastikan Anda telah menginstal dependensi berikut :

    1. Python 3.7 atau lebih baru
    2. 'python-telegram-bot' versi 20.x.x
    3. 'python-dotenv' untuk mengelola variabel lingkungan

Anda dapat menginstal dependensi dengan perintah berikut:

```sh
pip install python-telegram-bot python-dotenv
```

## Note

- **Keamanan Token** : Pastikan untuk tidak mengunggah file `.env` yang berisi token bot ke repositori publik. Tambahkan `.env` ke `.gitignore` untuk mencegahnya di-commit.
