"""Known-answer tests for Wednesday's connectors (seconds listed in time order)."""

from pathlib import Path

import pytest

from connectors.pipeline import total_hours
from connectors.sources import NetflixConnector, SpotifyConnector

DATA = Path(__file__).resolve().parent.parent / "data"


def test_spotify_seconds() -> None:
    sessions = SpotifyConnector(DATA / "spotify.json").load()
    assert [item.seconds for item in sessions] == pytest.approx([180.0, 240.5, 1800.0, 3.0])


def test_netflix_seconds_skip_trailers() -> None:
    sessions = NetflixConnector(DATA / "netflix.csv").load()
    assert [item.seconds for item in sessions] == pytest.approx([3723.0, 2710.0])


def test_total_hours_is_computed_per_source() -> None:
    hours = total_hours([SpotifyConnector(DATA / "spotify.json"), NetflixConnector(DATA / "netflix.csv")])
    assert hours["spotify"] == pytest.approx(2223.5 / 3600)
    assert hours["netflix"] == pytest.approx(6433.0 / 3600)
