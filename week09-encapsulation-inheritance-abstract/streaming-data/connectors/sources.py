"""Connectors for two real-world exports (Spotify and Netflix)."""

import csv
import json
from pathlib import Path

from connectors.base import Connector
from connectors.streaming import StreamingSession, hms_to_seconds, utc_from_iso, utc_from_netflix


class SpotifyConnector(Connector):
    """Spotify extended streaming history: a JSON list of plays."""

    def load(self) -> list[StreamingSession]:
        """loads the streaming sessions found in the Spotify JSON file"""
        plays = json.loads(self.path.read_text(encoding="utf-8"))

        # The export also holds your username and IP address. We never copy them.
        sessions = [
            StreamingSession(
                utc_from_iso(p["ts"]),
                p["master_metadata_track_name"] or p["episode_name"] or "(unknown)",
                p["ms_played"] / 1000,  # milliseconds -> seconds
                self.name,
            )
            for p in plays
        ]
        return sorted(sessions, key=lambda item: item.when)


class NetflixConnector(Connector):
    """Netflix ViewingActivity.csv: trailers skipped; all profiles unless one is given."""

    def __init__(self, path: Path, profile: str | None = None) -> None:
        super().__init__(path)
        self._profile = profile

    @property
    def profile(self) -> str | None:
        """Which Netflix profile to read (None = all). Fixed when the connector is created."""
        return self._profile

    def load(self) -> list[StreamingSession]:
        """Loads the streaming sessions found in the Netflix CSV file"""

        with self.path.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))

        sessions = [
            StreamingSession(utc_from_netflix(r["Start Time"]), r["Title"], hms_to_seconds(r["Duration"]), self.name)
            for r in rows
            if r["Supplemental Video Type"] == ""  # a trailer is not "viewing"
            and (self._profile is None or r["Profile Name"] == self._profile)
        ]

        return sorted(sessions, key=lambda item: item.when)
