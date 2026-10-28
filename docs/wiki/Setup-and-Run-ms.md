# Persediaan dan Menjalankan

🌐 **English** · [Dansk](Setup-and-Run-da) · [Bahasa Melayu](Setup-and-Run-ms)

## Apa yang anda perlukan

- Python 3.13 atau lebih baharu.
- Untuk langkah 2 hingga 4: akaun Google dan Firefox.

## Cipta persekitaran maya

```bash
python -m venv .venv
```

Aktifkannya. Pada Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Pada Linux dan macOS:

```bash
source .venv/bin/activate
```

Naik taraf `pip` dan pasang projek:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Cipta `browser.json`

`ytmusicapi` tidak mempunyai kunci API. Ia menggunakan semula log masuk pelayar anda, jadi anda menyalin pengepala permintaan bagi sesi yang telah log masuk sekali sahaja.

1. Buka Firefox dan pergi ke <https://music.youtube.com>, dalam keadaan telah log masuk.
2. Buka alat pembangun (`Ctrl+Shift+I`, pada macOS `Cmd+Option+I`) dan pilih **Network**.
3. Taip `browse` dalam penapis, pilih satu permintaan `browse?...` yang berjaya, klik kanan padanya dan pilih *Copy Value*, kemudian *Copy Request Headers*.
4. Jalankan `ytmusicapi browser` dalam folder projek dan tampal pengepala tersebut. Akhiri dengan `Ctrl+D` (`Ctrl+Z` dan Enter pada Windows). Pada macOS jalankan `pbpaste | ytmusicapi browser`.

Fail ini mengandungi kuki anda: ia diabaikan oleh git dan tidak boleh dikongsi sama sekali. Kuki akan tamat tempoh selepas beberapa lama; ulangi langkah-langkah ini untuk mendapatkan fail yang baharu.

## Jalankan

```bash
python -m musical_time_machine --list-only      # step 1: print the chart
python -m musical_time_machine --check-login    # step 2: count your playlists
python -m musical_time_machine --create-playlist  # step 3: create the playlist
python -m musical_time_machine                  # step 4: the full program
```

Format tarikh ialah `YYYY-MM-DD`; gunakan tarikh yang ada pada Bakeboard, contohnya `2026-04-18`.

## Uji

```bash
python -m pytest
```

Ujian tidak memerlukan rangkaian dan tidak memerlukan akaun.
