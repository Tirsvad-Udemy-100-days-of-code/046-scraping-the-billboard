"""@file
@brief All constants of the Musical Time Machine, defined once.
"""

from typing import Final

## @name Chart source
## @{

## @brief Base URL of the Bakeboard Hot 100 clone; the chart date and a slash are appended.
BASE_URL: Final[str] = "https://appbrewery.github.io/bakeboard-hot-100/"

## @brief strptime/strftime format of the chart date the user enters.
DATE_FORMAT: Final[str] = "%Y-%m-%d"

## @brief Number of entries on one Hot 100 chart.
CHART_SIZE: Final[int] = 100
## @}

## @name HTTP request
## @{

## @brief Headers sent with every chart request.
REQUEST_HEADERS: Final[dict[str, str]] = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ),
}

## @brief Seconds to wait for the chart page before giving up.
REQUEST_TIMEOUT_SECONDS: Final[int] = 10
## @}

## @name CSS selectors of the Bakeboard chart markup
## @{

## @brief One chart row.
SELECTOR_ROW: Final[str] = "div.chart-entry"

## @brief Song title inside a row.
SELECTOR_TITLE: Final[str] = "h3.chart-entry__title"

## @brief Artist inside a row.
SELECTOR_ARTIST: Final[str] = "span.chart-entry__artist"
## @}

## @name Command line
## @{

## @brief Prompt asking for the chart date.
DATE_PROMPT: Final[str] = (
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

## @brief Message for a date that is not YYYY-MM-DD; format with the entered text.
INVALID_DATE_MESSAGE: Final[str] = "'{text}' is not a valid date; use the format YYYY-MM-DD."

## @brief Message when the chart page cannot be fetched; format with the cause.
CHART_UNAVAILABLE_MESSAGE: Final[str] = "The chart could not be fetched: {reason}"

## @brief Message when the page holds no songs; format with the chart date.
CHART_PARSE_MESSAGE: Final[str] = "No songs were found on the chart page for {date}."

## @brief Line format of the printed song list.
SONG_LINE_TEMPLATE: Final[str] = "{position}. {title} - {artist}"

## @brief Process exit code on success.
EXIT_OK: Final[int] = 0

## @brief Process exit code when a domain error stopped the run.
EXIT_FAILURE: Final[int] = 1
## @}

## @name YouTube Music
## @{

## @brief Playlist title; format with the chart date.
PLAYLIST_NAME_TEMPLATE: Final[str] = "{date} Billboard 100"

## @brief Playlist description; format with the chart date.
PLAYLIST_DESCRIPTION_TEMPLATE: Final[str] = (
    "Billboard Hot 100 of {date}, made by Musical Time Machine."
)

## @brief File holding the ytmusicapi browser authentication headers (git-ignored).
BROWSER_FILE_NAME: Final[str] = "browser.json"

## @brief ytmusicapi search filter, so only songs are matched.
SEARCH_FILTER: Final[str] = "songs"

## @brief Privacy status of the created playlist.
PLAYLIST_PRIVACY: Final[str] = "PRIVATE"
## @}
