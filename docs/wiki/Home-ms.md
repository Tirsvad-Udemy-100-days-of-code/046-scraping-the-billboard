# Musical Time Machine

🌐 **English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

Penyelesaian untuk hari ke-46 kursus Udemy *100 Days of Code: The Complete Python Pro Bootcamp*. Taip satu tarikh, dan program ini mengikis web (scraping) Billboard Hot 100 pada hari itu, lalu membina senarai main YouTube Music yang peribadi daripada lagu-lagu tersebut, supaya anda dapat mendengar muzik pada hari yang bermakna bagi anda.

Wiki ini mengikuti empat langkah dalam kuliah. Setiap halaman menunjukkan apa yang dilakukan oleh langkah itu, satu tangkapan skrin, dan **apa yang kita pelajari**: teknik yang diajar oleh langkah tersebut.

| Halaman | Baca apabila anda mahu |
| --- | --- |
| [Persediaan dan Menjalankan](Setup-and-Run-ms) | Memasang projek dalam `.venv`, mencipta `browser.json` dan menjalankan ujian |
| [Langkah 1 - Mengikis Billboard Hot 100](Step-1-Scrape-the-Billboard-ms) | Melihat bagaimana `requests` dan `BeautifulSoup` menukar laman web menjadi senarai Python |
| [Langkah 2 - Pengesahan YouTube Music](Step-2-YouTube-Music-Authentication-ms) | Melihat bagaimana `ytmusicapi` meminjam log masuk pelayar anda |
| [Langkah 3 - Mencipta Senarai Main](Step-3-Create-the-Playlist-ms) | Melihat cara mencipta sesuatu sekali sahaja dan tidak pernah dua kali |
| [Langkah 4 - Mencari dan Menambah Lagu](Step-4-Search-and-Add-Songs-ms) | Melihat bagaimana gelung yang panjang terus berjalan apabila satu item gagal |

## Gambaran keseluruhan

| Lapisan | Kandungannya |
| --- | --- |
| `domain` | `Song`, `Playlist`, peraturan tarikh dan ralat |
| `application` | Kes penggunaan (`scrape_titles`, `create_playlist`, `add_songs`) dan port yang diperlukannya |
| `infrastructure` | Pengikis Bakeboard dan penyesuai `ytmusicapi` |
| `presentation` | Baris perintah, yang menghubungkan segala-galanya |

Setiap pemalar berada dalam `constants.py`. Ujian menggunakan salinan tersimpan bagi laman carta dan YouTube Music tiruan, jadi ia tidak memerlukan rangkaian atau akaun.

## Tangkapan skrin

Tangkapan skrin langkah 1 ialah larian sebenar. Tangkapan skrin langkah 2 hingga 4 menunjukkan larian tanpa `browser.json` dan ujian dengan YouTube Music tiruan; tangkapan skrin langsung akan ditambah apabila penulis telah mencipta `browser.json`.
