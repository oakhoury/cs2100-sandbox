"""Polymorphism in action: this function never asks which connector class it was given."""

from collections.abc import Sequence

from connectors.base import Connector


def total_hours(connectors: Sequence[Connector]) -> dict[str, float]:
    """Hours per source."""
    hours: dict[str, float] = {}
    for connector in connectors:
        for listen in connector.load():
            hours[listen.source] = hours.get(listen.source, 0.0) + listen.seconds / 3600
    return hours
