# Trin 2 - YouTube Music-godkendelse

🌐 **English** · [Dansk](Step-2-YouTube-Music-Authentication-da) · [Bahasa Melayu](Step-2-YouTube-Music-Authentication-ms)

## Hvad trinnet gør

YouTube Music har ingen enkel API-nøgle. Biblioteket `ytmusicapi` virker ved at låne din browsers login: du kopierer anmodningshovederne fra en logget ind Firefox-session én gang (se [Setup og kørsel](Setup-and-Run-da)), og `ytmusicapi browser` gør dem til `browser.json`. Programmet åbner derefter `YTMusic("browser.json")` og tæller afspilningslisterne i dit bibliotek.

```bash
python -m musical_time_machine --check-login
```

Ved succes udskriver det `Found N playlists in your library.` Uden en gyldig `browser.json` udskriver det trinnene til fornyelse og afslutter med kode 1 i stedet for at vise et stack trace.

Skærmbilledet viser kørslen **uden** `browser.json` og de tests, der bruger en falsk YouTube Music-tjeneste. Et rigtigt skærmbillede tilføjes, når `browser.json` findes.

![Login-tjek uden browser.json og testene til trin 2](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step2-check-login.png)

## Det lærte vi

- **Hvordan cookie-baseret godkendelse virker.** Din browser beviser, hvem du er, med cookies og hoveder på hver anmodning; ved at kopiere dem kan et script optræde som den session. Det er også derfor, `browser.json` er en hemmelighed, ignoreres af git og udløber efter et stykke tid.
- **At skjule et bibliotek bag en port.** Programmet taler med interfacet `MusicService`; kun `infrastructure/ytmusic.py` importerer `ytmusicapi`. Testene bruger en falsk tjeneste, og en anden musiktjeneste kunne tage dens plads.
- **At fejle hjælpsomt.** En manglende eller udløbet fil bliver til en tydelig besked, der siger, hvordan den fornyes, fordi den fejl, en bruger ser, er en del af produktet.
- **En doven forbindelse.** Klienten oprettes ved første brug, så opbygningen af tjenesten aldrig rører netværket.
