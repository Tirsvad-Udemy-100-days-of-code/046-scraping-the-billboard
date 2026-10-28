# Setup og kørsel

🌐 **English** · [Dansk](Setup-and-Run-da) · [Bahasa Melayu](Setup-and-Run-ms)

## Hvad du skal bruge

- Python 3.13 eller nyere.
- Til trin 2 til 4: en Google-konto og Firefox.

## Opret det virtuelle miljø

```bash
python -m venv .venv
```

Aktivér det. I Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

På Linux og macOS:

```bash
source .venv/bin/activate
```

Opgradér `pip` og installér projektet:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Opret `browser.json`

`ytmusicapi` har ingen API-nøgle. Biblioteket genbruger din browsers login, så du kopierer anmodningshovederne (request headers) fra en logget ind session én gang.

1. Åbn Firefox og gå til <https://music.youtube.com>, logget ind.
2. Åbn udviklerværktøjerne (`Ctrl+Shift+I`, på macOS `Cmd+Option+I`) og vælg **Network**.
3. Skriv `browse` i filteret, vælg en vellykket `browse?...`-anmodning, højreklik på den og vælg *Copy Value* og derefter *Copy Request Headers*.
4. Kør `ytmusicapi browser` i projektmappen og indsæt hovederne. Afslut med `Ctrl+D` (`Ctrl+Z` og Enter på Windows). På macOS kører du `pbpaste | ytmusicapi browser`.

Filen indeholder dine cookies: den ignoreres af git og må aldrig deles. Cookies udløber efter et stykke tid; gentag trinnene for at få en ny fil.

**Hvis `--check-login` siger `Expecting value`**, indeholder filen poster, der ikke er anmodningshoveder (en kopi fra Chrome kan tilføje `Request URL`, `Decoded`, `music.youtube.com`, en sti eller `content-encoding`). Kopiér kun blokken **Request Headers**, eller brug Firefox' *Copy Request Headers*, og opret filen igen.

## Kørsel

```bash
python -m musical_time_machine --list-only      # step 1: print the chart
python -m musical_time_machine --check-login    # step 2: count your playlists
python -m musical_time_machine --create-playlist  # step 3: create the playlist
python -m musical_time_machine                  # step 4: the full program
```

Datoformatet er `YYYY-MM-DD`; brug en dato, som Bakeboard har, for eksempel `2026-04-18`.

## Test

```bash
python -m pytest
```

Testene kræver hverken netværk eller konto.
