# Langkah 2 - Pengesahan YouTube Music

🌐 **English** · [Dansk](Step-2-YouTube-Music-Authentication-da) · [Bahasa Melayu](Step-2-YouTube-Music-Authentication-ms)

## Apa yang dilakukan oleh langkah ini

YouTube Music tidak mempunyai kunci API yang mudah. Pustaka `ytmusicapi` berfungsi dengan meminjam log masuk pelayar anda: anda menyalin pengepala permintaan bagi sesi Firefox yang telah log masuk sekali sahaja (lihat [Persediaan dan Menjalankan](Setup-and-Run-ms)), dan `ytmusicapi browser` menukarnya menjadi `browser.json`. Program kemudian membuka `YTMusic("browser.json")` dan mengira senarai main dalam pustaka anda.

```bash
python -m musical_time_machine --check-login
```

Jika berjaya, ia mencetak `Found N playlists in your library.` Tanpa `browser.json` yang sah, ia mencetak langkah pembaharuan dan keluar dengan kod 1, dan bukannya jejak tindanan.

Tangkapan skrin menunjukkan larian **tanpa** `browser.json` dan ujian yang menggunakan YouTube Music tiruan. Tangkapan skrin langsung akan ditambah apabila `browser.json` wujud.

![Semakan log masuk tanpa browser.json, dan ujian langkah 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step2-check-login.png)

## Apa yang kita pelajari

- **Bagaimana pengesahan berasaskan kuki berfungsi.** Pelayar anda membuktikan siapa anda dengan kuki dan pengepala pada setiap permintaan; menyalinnya membolehkan skrip bertindak sebagai sesi itu. Itulah juga sebabnya `browser.json` ialah rahsia, diabaikan oleh git dan tamat tempoh selepas beberapa lama.
- **Menyembunyikan pustaka di sebalik port.** Program berinteraksi dengan antara muka `MusicService`; hanya `infrastructure/ytmusic.py` yang mengimport `ytmusicapi`. Ujian menggunakan perkhidmatan tiruan, dan perkhidmatan muzik lain boleh menggantikannya.
- **Gagal dengan membantu.** Fail yang hilang atau tamat tempoh menjadi mesej yang jelas yang menerangkan cara memperbaharuinya, kerana ralat yang dilihat pengguna ialah sebahagian daripada produk.
- **Sambungan malas.** Klien dicipta pada penggunaan pertama, jadi membina perkhidmatan tidak pernah menyentuh rangkaian.
