"""@file
@brief Ports the use cases need from the outside world.
"""

from datetime import date
from typing import Protocol

from musical_time_machine.domain.song import Song


class ChartSource(Protocol):
    """@brief Supplies the songs of one chart."""

    def songs_for(self, chart_date: date) -> list[Song]:
        """@brief Get the songs of the chart of a date.

        @param chart_date Date of the chart.
        @return The songs in chart order.
        """
        ...
