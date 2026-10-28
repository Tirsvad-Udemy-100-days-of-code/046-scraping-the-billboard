"""@file
@brief Validation of the chart date.
"""

from datetime import date, datetime

from musical_time_machine.constants import DATE_FORMAT, INVALID_DATE_MESSAGE
from musical_time_machine.domain.errors import InvalidChartDateError


def parse_chart_date(text: str) -> date:
    """@brief Turn YYYY-MM-DD text into a date.

    @param text The text the user entered.
    @return The calendar date.
    @throws InvalidChartDateError when the text is not a real date in that format.
    """
    cleaned = text.strip()
    try:
        parsed = datetime.strptime(cleaned, DATE_FORMAT).date()
    except ValueError as error:
        raise InvalidChartDateError(INVALID_DATE_MESSAGE.format(text=cleaned)) from error
    if parsed.strftime(DATE_FORMAT) != cleaned:
        # strptime accepts "2026-4-8"; the contract is the zero-padded form.
        raise InvalidChartDateError(INVALID_DATE_MESSAGE.format(text=cleaned))
    return parsed
