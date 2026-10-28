"""@file
@brief The Song value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Song:
    """@brief One chart entry.

    @param title Song title.
    @param artist Performing artist.
    """

    title: str
    artist: str
