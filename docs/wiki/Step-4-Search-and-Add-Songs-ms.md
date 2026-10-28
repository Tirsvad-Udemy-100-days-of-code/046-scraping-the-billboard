# Langkah 4 - Mencari dan Menambah Lagu

🌐 **English** · [Dansk](Step-4-Search-and-Add-Songs-da) · [Bahasa Melayu](Step-4-Search-and-Add-Songs-ms)

## Apa yang dilakukan oleh langkah ini

Untuk setiap lagu dalam carta, program mencari di YouTube Music dengan tajuk dan artis, menggunakan `yt.search(query, filter="songs")` supaya hanya hasil lagu dikembalikan, dan menambah hasil teratas dengan `yt.add_playlist_items()`. Lagu yang tidak ditemui, atau yang gagal, dilangkau dan gelung diteruskan. Pada akhirnya program memberitahu berapa banyak lagu telah ditambah dan yang mana dilangkau.

```bash
python -m musical_time_machine
```

Tangkapan skrin menunjukkan ujian langkah ini dengan YouTube Music tiruan: semua lagu ditambah, dan lagu yang gagal dilangkau tanpa menghentikan larian. Tangkapan skrin langsung akan ditambah apabila `browser.json` wujud.

![Ujian langkah 4: lagu ditambah dan lagu yang gagal dilangkau](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step4-add-songs.png)

## Apa yang kita pelajari

- **Gelung yang bertahan menghadapi item yang buruk.** Satu lagu daripada seratus mempunyai tajuk yang ganjil atau tiada padanan. Menangkap ralat lagu yang khusus di dalam gelung, dan merekodkan apa yang dilangkau, menghalang satu kegagalan daripada menghilangkan sembilan puluh sembilan yang lain.
- **Mengetahui apa yang *tidak* perlu ditangkap.** Log masuk yang gagal akan menyebabkan setiap lagu berikutnya gagal juga, jadi ralat pengesahan tidak dilangkau: ia menghentikan larian. Menangkap segala-galanya dengan `except` kosong akan menyembunyikan perkara itu.
- **Memadankan carian dengan hasil.** Mencari "title artist" dengan penapis `songs` memberikan padanan lagu terbaik; hasil pertama ialah peraturan yang cukup baik untuk senarai main, dan hasil tidak ditemui ialah kesudahan biasa, bukan ralat.
- **Menguji masa.** Jeda antara panggilan disuntik, jadi ujian berjalan serta-merta dan masih membuktikan bahawa jeda itu berlaku.
- **Persembahan yang nipis.** Baris perintah hanya membaca input dan mencetak ringkasan; keseluruhan aliran ialah kes penggunaan `time_travel`, itulah sebabnya ia boleh diuji dari hujung ke hujung dengan perkhidmatan tiruan.
