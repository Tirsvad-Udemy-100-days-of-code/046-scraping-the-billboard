"""@file
@brief The Playlist value object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Playlist:
    """@brief One playlist of the user's library.

    @param playlist_id Identifier given by the music service.
    @param title Playlist title.
    """

    playlist_id: str
    title: str
