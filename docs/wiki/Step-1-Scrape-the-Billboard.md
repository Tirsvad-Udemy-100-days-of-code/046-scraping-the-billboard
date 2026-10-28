# Step 1 - Scrape the Billboard Hot 100

🌐 **English** · [Dansk](Step-1-Scrape-the-Billboard-da) · [Bahasa Melayu](Step-1-Scrape-the-Billboard-ms)

## What the step does

The program asks for a date in the format `YYYY-MM-DD`, requests `https://appbrewery.github.io/bakeboard-hot-100/<date>/` and reads the 100 songs out of the HTML. Bakeboard is the course's clone of the Billboard Hot 100, because the real site can change or add a paywall at any time.

```bash
python -m musical_time_machine --list-only
```

The Bakeboard page of 2026-04-18:

![The Bakeboard Hot 100 page for 2026-04-18](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step1-bakeboard-page.png)

The output of the program (rendered from the text of a real run, not a photo of a terminal window):

![Output of step 1 for 2026-04-18](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/046-scraping-the-billboard/raw/branch/main/docs/wiki/images/step1-terminal-output.png)

## What we gained

- **Reading a web page as data.** `BeautifulSoup` turns HTML into a tree, and a CSS selector (`div.chart-entry`, `h3.chart-entry__title`) picks the parts we want. We found the selectors by looking at the page's markup first.
- **Being a polite client.** A request carries headers; the `User-Agent` tells the server what kind of client asks. A `timeout` and `raise_for_status()` make a slow or missing page fail clearly instead of hanging.
- **Validating input at the edge.** `parse_chart_date` accepts only real `YYYY-MM-DD` dates, so the rest of the program never sees a bad date.
- **Testing without the network.** The chart page is stored under `tests/fixtures/`, and the scraper takes its page fetcher as a parameter, so the tests check 100 songs without a single request.
- **Keeping the knowledge in one place.** URL, selectors and messages live in `constants.py`; if Bakeboard changes its markup, one file changes.
