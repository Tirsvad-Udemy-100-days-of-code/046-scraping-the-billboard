# Musical Time Machine

🌐 **English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

A solution to day 46 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*. Type a date, and the program scrapes the Billboard Hot 100 of that day and builds a private YouTube Music playlist from the songs, so you can listen to the music of a day that matters to you.

The wiki follows the four steps of the lecture. Each page shows what the step does, a screenshot, and **what we gained**: the technique the step teaches.

| Page | Read it when you want to |
| --- | --- |
| [Setup and Run](Setup-and-Run) | Install the project in a `.venv`, create `browser.json` and run the tests |
| [Step 1 - Scrape the Billboard Hot 100](Step-1-Scrape-the-Billboard) | See how `requests` and `BeautifulSoup` turn a web page into a Python list |
| [Step 2 - YouTube Music Authentication](Step-2-YouTube-Music-Authentication) | See how `ytmusicapi` borrows your browser's login |
| [Step 3 - Create the Playlist](Step-3-Create-the-Playlist) | See how to create something once and never twice |
| [Step 4 - Search and Add Songs](Step-4-Search-and-Add-Songs) | See how a long loop keeps going when one item fails |

## Overview

| Layer | What it holds |
| --- | --- |
| `domain` | `Song`, `Playlist`, the date rules and the errors |
| `application` | The use cases (`scrape_titles`, `create_playlist`, `add_songs`) and the ports they need |
| `infrastructure` | The Bakeboard scraper and the `ytmusicapi` adapter |
| `presentation` | The command line, which connects everything |

Every constant is in `constants.py`. The tests use a stored copy of the chart page and a fake YouTube Music, so they never need the network or an account.

## Screenshots

Every step has a screenshot of a real run. For steps 2 to 4 the live run uses the author's `browser.json` (it is never published), and a second screenshot shows the tests with a fake YouTube Music.
