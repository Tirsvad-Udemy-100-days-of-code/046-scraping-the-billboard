"""@file
@brief Tests of the count_library_playlists use case.
"""

import pytest
from conftest import FakeMusicService

from musical_time_machine.application.use_cases import count_library_playlists
from musical_time_machine.domain.errors import AuthenticationError
from musical_time_machine.domain.playlist import Playlist


def test_count_library_playlists_returns_number_of_playlists() -> None:
    service = FakeMusicService([Playlist("a", "A"), Playlist("b", "B")])

    assert count_library_playlists(service) == 2


def test_count_library_playlists_returns_zero_for_empty_library() -> None:
    assert count_library_playlists(FakeMusicService()) == 0


def test_count_library_playlists_propagates_authentication_error() -> None:
    with pytest.raises(AuthenticationError):
        count_library_playlists(FakeMusicService(error=AuthenticationError("no")))
