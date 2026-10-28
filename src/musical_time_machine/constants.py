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

## @name Login check
## @{

## @brief Message with the number of library playlists; format with the count.
PLAYLIST_COUNT_MESSAGE: Final[str] = "Found {count} playlists in your library."

## @brief Message when browser.json is missing or rejected; format with reason and file.
BROWSER_RENEWAL_MESSAGE: Final[str] = (
    "YouTube Music login failed: {reason}\n"
    "To create or renew {file}:\n"
    "  1. Open Firefox and go to https://music.youtube.com while logged in.\n"
    "  2. Open the developer tools (F12) and select the Network tab.\n"
    "  3. Filter the requests by 'browse' and select one POST request.\n"
    "  4. Right-click it and choose Copy Request Headers.\n"
    "  5. Run 'ytmusicapi browser' and paste the headers "
    "(macOS: pbpaste | ytmusicapi browser)."
)

## @brief Reason when the browser file does not exist; format with the file.
BROWSER_FILE_MISSING_REASON: Final[str] = "{file} was not found."

## @brief Command line flag that checks the YouTube Music login.
CHECK_LOGIN_FLAG: Final[str] = "--check-login"

## @brief Help text of the check-login flag.
CHECK_LOGIN_HELP: Final[str] = "Log in to YouTube Music and print the number of library playlists."

## @brief Command line flag that names the browser file.
BROWSER_FILE_FLAG: Final[str] = "--browser-file"

## @brief Help text of the browser-file flag.
BROWSER_FILE_HELP: Final[str] = "Path of the ytmusicapi browser headers file."
## @}

## @name Create playlist
## @{

## @brief Command line flag that creates the dated playlist.
CREATE_PLAYLIST_FLAG: Final[str] = "--create-playlist"

## @brief Help text of the create-playlist flag.
CREATE_PLAYLIST_HELP: Final[str] = (
    "Create the private playlist '<date> Billboard 100' in YouTube Music."
)

## @brief Message after a playlist was created; format with the title.
PLAYLIST_CREATED_MESSAGE: Final[str] = 'Created playlist "{title}".'

## @brief Message when the playlist already exists; format with the title.
PLAYLIST_EXISTS_MESSAGE: Final[str] = 'Playlist "{title}" already exists; nothing was created.'

## @brief Message when YouTube Music returned no playlist id; format with the answer.
PLAYLIST_CREATION_FAILED_MESSAGE: Final[str] = "The playlist could not be created: {reason}"
## @}

## @name Add songs
## @{

## @brief Seconds to wait between two songs, to stay gentle with YouTube Music.
ADD_PAUSE_SECONDS: Final[float] = 0.2

## @brief Number of search results to ask for; only the first is used.
SEARCH_LIMIT: Final[int] = 1

## @brief Status text ytmusicapi reports when songs were added.
STATUS_SUCCEEDED: Final[str] = "STATUS_SUCCEEDED"

## @brief HTTP status codes that mean the login was rejected.
AUTH_HTTP_CODES: Final[tuple[str, ...]] = ("HTTP 401", "HTTP 403")

## @brief Message when a search fails; format with the reason.
SONG_SEARCH_FAILED_MESSAGE: Final[str] = "The song search failed: {reason}"

## @brief Message when a song is not added; format with the answer.
SONG_ADD_FAILED_MESSAGE: Final[str] = "The song could not be added: {reason}"

## @brief Command line flag that only prints the chart songs.
LIST_ONLY_FLAG: Final[str] = "--list-only"

## @brief Help text of the list-only flag.
LIST_ONLY_HELP: Final[str] = "Only print the numbered chart songs; no YouTube Music login."

## @brief Summary line; format with added, total, title and skipped.
SUMMARY_MESSAGE: Final[str] = 'Added {added} of {total} songs to "{title}"; skipped {skipped}.'

## @brief One line per skipped song; format with title and artist.
SKIPPED_SONG_MESSAGE: Final[str] = "Skipped: {title} - {artist}"
## @}
