# Langkah 1 - Mengikis Billboard Hot 100

🌐 **English** · [Dansk](Step-1-Scrape-the-Billboard-da) · [Bahasa Melayu](Step-1-Scrape-the-Billboard-ms)

## Apa yang dilakukan oleh langkah ini

Program meminta satu tarikh dalam format `YYYY-MM-DD`, membuat permintaan ke `https://appbrewery.github.io/bakeboard-hot-100/<date>/` dan membaca 100 lagu daripada HTML. Bakeboard ialah klon Billboard Hot 100 yang disediakan kursus, kerana laman sebenar boleh berubah atau menambah tembok bayaran pada bila-bila masa.

```bash
python -m musical_time_machine --list-only
```

Laman Bakeboard bagi 2026-04-18:

![Laman Bakeboard Hot 100 untuk 2026-04-18](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step1-bakeboard-page.png)

Output program (dipaparkan daripada teks larian sebenar, bukan gambar tetingkap terminal):

![Output langkah 1 untuk 2026-04-18](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step1-terminal-output.png)

## Apa yang kita pelajari

- **Membaca laman web sebagai data.** `BeautifulSoup` menukar HTML menjadi pepohon, dan pemilih CSS (`div.chart-entry`, `h3.chart-entry__title`) memilih bahagian yang kita mahu. Kita menemui pemilih tersebut dengan melihat penanda halaman terlebih dahulu.
- **Menjadi klien yang sopan.** Sesuatu permintaan membawa pengepala; `User-Agent` memberitahu pelayan jenis klien yang meminta. `timeout` dan `raise_for_status()` menjadikan halaman yang perlahan atau tiada gagal dengan jelas dan bukannya tergantung.
- **Mengesahkan input di sempadan.** `parse_chart_date` hanya menerima tarikh `YYYY-MM-DD` yang sebenar, jadi bahagian lain program tidak pernah menerima tarikh yang salah.
- **Menguji tanpa rangkaian.** Laman carta disimpan di bawah `tests/fixtures/`, dan pengikis menerima pengambil halamannya sebagai parameter, jadi ujian memeriksa 100 lagu tanpa satu permintaan pun.
- **Menyimpan pengetahuan di satu tempat.** URL, pemilih dan mesej berada dalam `constants.py`; jika Bakeboard mengubah penandanya, hanya satu fail yang berubah.
