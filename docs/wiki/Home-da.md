# Musical Time Machine

🌐 **English** · [Dansk](Home-da) · [Bahasa Melayu](Home-ms)

En løsning på dag 46 i Udemys *100 Days of Code: The Complete Python Pro Bootcamp*. Skriv en dato, så scraper programmet Billboard Hot 100 for den dag (scraping betyder, at et program automatisk henter og læser data fra en hjemmeside) og bygger en privat YouTube Music-playliste af sangene, så du kan høre musikken fra en dag, der betyder noget for dig.

Wikien følger forelæsningens fire trin. Hver side viser, hvad trinnet gør, et skærmbillede og **Det lærte vi**: den teknik, trinnet lærer os.

| Side | Læs den, når du vil |
| --- | --- |
| [Setup og kørsel](Setup-and-Run-da) | Installere projektet i et `.venv`, oprette `browser.json` og køre testene |
| [Trin 1 - Scrape Billboard Hot 100](Step-1-Scrape-the-Billboard-da) | Se, hvordan `requests` og `BeautifulSoup` gør en hjemmeside til en Python-liste |
| [Trin 2 - YouTube Music-godkendelse](Step-2-YouTube-Music-Authentication-da) | Se, hvordan `ytmusicapi` låner din browsers login |
| [Trin 3 - Opret playlisten](Step-3-Create-the-Playlist-da) | Se, hvordan man opretter noget én gang og aldrig to |
| [Trin 4 - Søg efter og tilføj sange](Step-4-Search-and-Add-Songs-da) | Se, hvordan en lang løkke kører videre, når ét element fejler |

## Overblik

| Lag | Hvad det indeholder |
| --- | --- |
| `domain` | `Song`, `Playlist`, datoreglerne og fejlene |
| `application` | Use cases (`scrape_titles`, `create_playlist`, `add_songs`) og de porte, de har brug for |
| `infrastructure` | Bakeboard-scraperen og `ytmusicapi`-adapteren |
| `presentation` | Kommandolinjen, som forbinder det hele |

Alle konstanter ligger i `constants.py`. Testene bruger en gemt kopi af hitlistesiden og en falsk YouTube Music-tjeneste, så de aldrig har brug for netværket eller en konto.

## Skærmbilleder

Skærmbillederne af trin 1 er fra en rigtig kørsel. Skærmbillederne af trin 2 til 4 viser kørslen uden `browser.json` og testene med en falsk YouTube Music-tjeneste; rigtige skærmbilleder tilføjes, når forfatteren har oprettet `browser.json`.
