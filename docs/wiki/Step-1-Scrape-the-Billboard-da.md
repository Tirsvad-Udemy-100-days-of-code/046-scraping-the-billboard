# Trin 1 - Scrape Billboard Hot 100

🌐 **English** · [Dansk](Step-1-Scrape-the-Billboard-da) · [Bahasa Melayu](Step-1-Scrape-the-Billboard-ms)

## Hvad trinnet gør

Programmet beder om en dato i formatet `YYYY-MM-DD`, henter `https://appbrewery.github.io/bakeboard-hot-100/<date>/` og læser de 100 sange ud af HTML'en. Bakeboard er kursets kopi af Billboard Hot 100, fordi den rigtige side kan ændre sig eller få en betalingsmur når som helst.

```bash
python -m musical_time_machine --list-only
```

Bakeboard-siden for 2026-04-18:

![Bakeboard Hot 100-siden for 2026-04-18](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step1-bakeboard-page.png)

Programmets output (gengivet ud fra teksten fra en rigtig kørsel, ikke et foto af et terminalvindue):

![Output fra trin 1 for 2026-04-18](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step1-terminal-output.png)

## Det lærte vi

- **At læse en hjemmeside som data.** `BeautifulSoup` gør HTML til et træ, og en CSS-selektor (`div.chart-entry`, `h3.chart-entry__title`) udpeger de dele, vi vil have. Vi fandt selektorerne ved først at se på sidens markup.
- **At være en høflig klient.** En anmodning har hoveder (headers); `User-Agent` fortæller serveren, hvilken slags klient der spørger. En `timeout` og `raise_for_status()` får en langsom eller manglende side til at fejle tydeligt i stedet for at hænge.
- **At validere input ved grænsen.** `parse_chart_date` accepterer kun rigtige `YYYY-MM-DD`-datoer, så resten af programmet aldrig ser en ugyldig dato.
- **At teste uden netværk.** Hitlistesiden er gemt under `tests/fixtures/`, og scraperen tager sin sidehenter som parameter, så testene kontrollerer 100 sange uden en eneste anmodning.
- **At samle viden ét sted.** URL, selektorer og beskeder ligger i `constants.py`; hvis Bakeboard ændrer sit markup, er det én fil, der ændres.
