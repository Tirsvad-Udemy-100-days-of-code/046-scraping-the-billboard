# Trin 4 - Søg efter og tilføj sange

🌐 **English** · [Dansk](Step-4-Search-and-Add-Songs-da) · [Bahasa Melayu](Step-4-Search-and-Add-Songs-ms)

## Hvad trinnet gør

For hver sang på hitlisten søger programmet på YouTube Music med titlen og kunstneren, med `yt.search(query, filter="songs")`, så der kun kommer sangresultater tilbage, og tilføjer det øverste resultat med `yt.add_playlist_items()`. En sang, der ikke findes, eller som fejler, springes over, og løkken fortsætter. Til sidst fortæller programmet, hvor mange sange der blev tilføjet, og hvilke der blev sprunget over.

```bash
python -m musical_time_machine
```

En rigtig kørsel med forfatterens `browser.json`: alle 100 sange blev tilføjet:

![Rigtig kørsel: hele programmet](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step4-live-add-songs.png)

Skærmbilledet viser testene til dette trin med en falsk YouTube Music-tjeneste: alle sange tilføjes, og en sang, der fejler, springes over uden at stoppe kørslen.

![Tests af trin 4: sange tilføjes, og en sang, der fejler, springes over](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step4-add-songs.png)

## Det lærte vi

- **En løkke, der overlever dårlige elementer.** Én sang ud af hundrede har en mærkelig titel eller intet match. Når vi fanger de specifikke sangfejl inde i løkken og noterer, hvad der blev sprunget over, mister vi ikke de andre ni og halvfems på grund af én fejl.
- **At vide, hvad man *ikke* skal fange.** Et mislykket login ville få alle de følgende sange til at fejle også, så godkendelsesfejl springes ikke over: de stopper kørslen. At fange alt med et bart `except` ville skjule det.
- **At matche en søgning med et resultat.** Når man søger "title artist" med filteret `songs`, får man det bedste sangmatch; det første resultat er en god nok regel til en playliste, og et resultat, der ikke blev fundet, er et normalt udfald, ikke en fejl.
- **At teste tid.** Pausen mellem kaldene injiceres, så testene kører øjeblikkeligt og stadig beviser, at den finder sted.
- **Tynd præsentation.** Kommandolinjen læser kun input og udskriver oversigten; hele forløbet er use casen `time_travel`, og derfor kan det testes fra ende til anden med falske tjenester.
