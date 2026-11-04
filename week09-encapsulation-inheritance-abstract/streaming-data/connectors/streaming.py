"""The one record every connector produces, plus three tiny parsing helpers.

Plumbing: skim it, don't study it. The interesting code is in the other files.
"""

from datetime import datetime, timezone
from typing import NamedTuple


class StreamingSession(NamedTuple):
    """One listening/viewing session. Immutable, like any tuple."""

    when: datetime  # when the session STARTED (timezone-aware, UTC)
    title: str
    seconds: float  # how long it lasted, in SECONDS
    source: str  # which app it came from


def utc_from_iso(text: str) -> datetime:
    """'2024-09-02T13:00:00Z' or '2024-09-04T07:30:00-04:00' -> aware UTC datetime."""
    return datetime.fromisoformat(text.replace("Z", "+00:00")).astimezone(timezone.utc)


def utc_from_netflix(text: str) -> datetime:
    """'2024-09-03 01:15:22' (already UTC, no marker) -> aware UTC datetime."""
    return datetime.strptime(text, "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)


def hms_to_seconds(text: str) -> float:
    """'01:02:03' -> 3723.0"""
    hours, minutes, seconds = (int(part) for part in text.split(":"))
    return float(hours * 3600 + minutes * 60 + seconds)
