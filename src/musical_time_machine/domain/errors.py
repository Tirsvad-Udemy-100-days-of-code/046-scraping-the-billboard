"""@file
@brief Errors raised by the business rules of the Musical Time Machine.
"""


class MusicalTimeMachineError(Exception):
    """@brief Base class of every domain error."""


class InvalidChartDateError(MusicalTimeMachineError):
    """@brief The entered text is not a valid YYYY-MM-DD date."""


class ChartUnavailableError(MusicalTimeMachineError):
    """@brief The chart page could not be fetched (missing page or HTTP error)."""


class ChartParseError(MusicalTimeMachineError):
    """@brief The chart page holds no songs."""


class BrowserFileMissingError(MusicalTimeMachineError):
    """@brief The browser authentication file does not exist."""


class AuthenticationError(MusicalTimeMachineError):
    """@brief YouTube Music rejected the browser authentication headers."""


class PlaylistCreationError(MusicalTimeMachineError):
    """@brief YouTube Music did not create the playlist."""
