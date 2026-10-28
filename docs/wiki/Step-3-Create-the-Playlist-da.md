# Trin 3 - Opret playlisten

🌐 **English** · [Dansk](Step-3-Create-the-Playlist-da) · [Bahasa Melayu](Step-3-Create-the-Playlist-ms)

## Hvad trinnet gør

Programmet opretter en privat playliste med navnet `{date} Billboard 100`, for eksempel `2026-04-18 Billboard 100`, med `yt.create_playlist(title, description, privacy_status="PRIVATE")`. Før det opretter noget, gennemløber det `yt.get_library_playlists()`; hvis der findes en playliste med samme titel, bruger det den.

```bash
python -m musical_time_machine --create-playlist
```

En rigtig kørsel med forfatterens `browser.json`: første kørsel opretter playlisten, anden kørsel opretter ingenting:

![Rigtig kørsel: playlisten oprettes to gange](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step3-live-create-playlist.png)

Skærmbilledet viser testene til dette trin med en falsk YouTube Music-tjeneste: det første kald opretter én playliste, og det andet kald for samme dato opretter ingen.

![Tests af trin 3: playlisten oprettes én gang](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step3-create-playlist.png)

## Det lærte vi

- **Idempotens.** En handling, du kan køre to gange med samme resultat, er sikker at gentage. Ved først at tjekke for en eksisterende playliste fylder et nedbrud eller en ekstra kørsel aldrig biblioteket med dubletter.
- **Ét sted for et navn.** Playlistens titel og beskrivelse bygges af skabeloner i `constants.py` af én funktion, så tjekket og oprettelsen aldrig kan være uenige om titlen.
- **At læse en API's rigtige svar.** `create_playlist` returnerer playlistens id ved succes, men en fejlordbog ved fejl; adapteren tjekker, hvilket af dem den fik, og rejser en tydelig fejl.
- **Privatliv som standard.** Når playlisten oprettes som `PRIVATE`, udgiver en testkørsel aldrig noget.
