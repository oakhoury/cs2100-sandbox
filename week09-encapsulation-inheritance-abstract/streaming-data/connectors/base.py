"""Wednesday: a plain base class that subclasses specialise."""

from pathlib import Path

from connectors.streaming import StreamingSession


class Connector:
    """Base class: reads one app's export and returns a list of StreamingSession records."""

    def __init__(self, path: Path) -> None:
        self._path = path

    @property
    def path(self) -> Path:
        """Where the export lives. Read-only: it is fixed when the connector is created."""
        return self._path

    @property
    def name(self) -> str:
        """Short label used in StreamingSession.source (default: the class name)."""
        return type(self).__name__.removesuffix("Connector").lower()

    def load(self) -> list[StreamingSession]:
        raise NotImplementedError(f"{type(self).__name__} must override load()")
