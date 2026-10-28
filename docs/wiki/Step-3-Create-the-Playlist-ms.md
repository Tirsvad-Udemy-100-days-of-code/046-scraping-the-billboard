# Langkah 3 - Mencipta Senarai Main

🌐 **English** · [Dansk](Step-3-Create-the-Playlist-da) · [Bahasa Melayu](Step-3-Create-the-Playlist-ms)

## Apa yang dilakukan oleh langkah ini

Program mencipta senarai main peribadi bernama `{date} Billboard 100`, contohnya `2026-04-18 Billboard 100`, dengan `yt.create_playlist(title, description, privacy_status="PRIVATE")`. Sebelum mencipta apa-apa, ia menggelung melalui `yt.get_library_playlists()`; jika senarai main dengan tajuk yang sama wujud, ia menggunakan yang itu.

```bash
python -m musical_time_machine --create-playlist
```

Tangkapan skrin menunjukkan ujian langkah ini dengan YouTube Music tiruan: panggilan pertama mencipta satu senarai main, panggilan kedua untuk tarikh yang sama tidak mencipta apa-apa. Tangkapan skrin langsung akan ditambah apabila `browser.json` wujud.

![Ujian langkah 3: senarai main dicipta sekali sahaja](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step3-create-playlist.png)

## Apa yang kita pelajari

- **Idempotensi.** Operasi yang boleh dijalankan dua kali dengan hasil yang sama selamat untuk diulang. Menyemak senarai main sedia ada terlebih dahulu bermakna ranap atau larian kedua tidak pernah memenuhi pustaka dengan pendua.
- **Satu tempat untuk sebuah nama.** Tajuk dan penerangan senarai main dibina daripada templat dalam `constants.py` oleh satu fungsi, jadi semakan dan penciptaan tidak akan pernah berbeza tentang tajuknya.
- **Membaca jawapan sebenar sesebuah API.** `create_playlist` mengembalikan id senarai main jika berjaya tetapi kamus ralat jika gagal; penyesuai menyemak yang mana satu diterima dan mencetuskan ralat yang jelas.
- **Privasi secara lalai.** Mencipta senarai main sebagai `PRIVATE` bermakna larian ujian tidak pernah menerbitkan apa-apa.
