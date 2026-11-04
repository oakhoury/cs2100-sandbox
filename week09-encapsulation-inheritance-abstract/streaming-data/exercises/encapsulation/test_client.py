"""Encapsulation: promise-named tests for StreamingClient.

On the broken starter (expect failures -- that is the point):
    pytest exercises/encapsulation
On the instructor solution (all pass):
    CLIENT_MODULE=solutions.client pytest exercises/encapsulation
"""

import importlib
import os
from typing import Any

import pytest

StreamingClient: Any = importlib.import_module(os.environ.get("CLIENT_MODULE", "client")).StreamingClient
TOKEN = "s3cr3t-token-123"


def make(**kwargs: Any) -> Any:
    return StreamingClient("ana", TOKEN, **kwargs)


def test_auth_header_still_works() -> None:
    assert make().auth_header() == {"Authorization": f"Bearer {TOKEN}"}


def test_rate_limit_is_enforced() -> None:
    client = make(rate_limit=1)
    client.fetch("/a")
    with pytest.raises(RuntimeError):
        client.fetch("/b")


def test_repr_hides_the_token() -> None:
    """Promise: the token never shows up when a client is printed or logged."""
    assert TOKEN not in repr(make())


def test_error_messages_hide_the_token() -> None:
    """Promise: failures (which end up in logs and bug reports) never contain the token."""
    client = make(rate_limit=1)
    client.fetch("/a")
    with pytest.raises(RuntimeError) as info:
        client.fetch("/b")
    assert TOKEN not in str(info.value)


def test_a_bad_rate_limit_is_rejected() -> None:
    with pytest.raises(ValueError):
        make(rate_limit=0)
    client = make()
    with pytest.raises(ValueError):
        client.rate_limit = 0


def test_request_count_is_read_only() -> None:
    """Promise: only fetch() changes the count -- nobody can reset it to dodge the limit."""
    client = make()
    with pytest.raises(AttributeError):
        client.request_count = 0


def test_token_is_not_part_of_the_public_api() -> None:
    public = {name for name in dir(make()) if not name.startswith("_")}
    assert public <= {"username", "rate_limit", "request_count", "auth_header", "fetch"}
