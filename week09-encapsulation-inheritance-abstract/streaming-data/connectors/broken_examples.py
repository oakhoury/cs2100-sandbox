"""Subclasses that misbehave on purpose."""

import csv

from connectors.base import Connector
from connectors.streaming import StreamingSession, utc_from_iso
from connectors.sources import SpotifyConnector


class FitTrackConnector(Connector):
    """A teammate's new connector for a fitness-app CSV. Looks fine... is it?"""

    def load(self) -> list[StreamingSession]:
        with self.path.open(newline="", encoding="utf-8") as file:
            rows = list(csv.DictReader(file))
        return [
            StreamingSession(utc_from_iso(r["Date"]), r["Activity"], float(r["Elapsed Time (min)"]), self.name)
            # BUG: minutes, not seconds -- no crash, wrong totals
            for r in rows
        ]


class ForgetfulConnector(Connector):
    """A connector whose author forgot to override load()."""


class QuietSpotifyConnector(SpotifyConnector):
    """A 'helpful' subclass that tidies the data by dropping rows with no title."""

    def load(self) -> list[StreamingSession]:
        return [session for session in super().load() if session.title != "(unknown)"]
