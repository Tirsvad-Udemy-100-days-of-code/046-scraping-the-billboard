# Setup and Run

🌐 **English** · [Dansk](Setup-and-Run-da) · [Bahasa Melayu](Setup-and-Run-ms)

## What you need

- Python 3.13 or later.
- For steps 2 to 4: a Google account and Firefox.

## Create the virtual environment

```bash
python -m venv .venv
```

Activate it. On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

On Linux and macOS:

```bash
source .venv/bin/activate
```

Upgrade `pip` and install the project:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Create `browser.json`

`ytmusicapi` has no API key. It reuses the login of your browser, so you copy the request headers of a logged-in session once.

1. Open Firefox and go to <https://music.youtube.com>, logged in.
2. Open the developer tools (`Ctrl+Shift+I`, on macOS `Cmd+Option+I`) and choose **Network**.
3. Type `browse` in the filter, pick a successful `browse?...` request, right-click it and choose *Copy Value*, then *Copy Request Headers*.
4. Run `ytmusicapi browser` in the project folder and paste the headers. Finish with `Ctrl+D` (`Ctrl+Z` and Enter on Windows). On macOS run `pbpaste | ytmusicapi browser`.

The file contains your cookies: it is ignored by git and must never be shared. The cookies expire after a while; repeat the steps for a fresh file.

## Run

```bash
python -m musical_time_machine --list-only      # step 1: print the chart
python -m musical_time_machine --check-login    # step 2: count your playlists
python -m musical_time_machine --create-playlist  # step 3: create the playlist
python -m musical_time_machine                  # step 4: the full program
```

The date format is `YYYY-MM-DD`; use a date that Bakeboard has, for example `2026-04-18`.

## Test

```bash
python -m pytest
```

The tests need no network and no account.
