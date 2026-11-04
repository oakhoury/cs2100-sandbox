"""Encapsulation (solution): a client that does not leak its secret."""


def _check(rate_limit: int) -> int:
    """Raises an error if rate_limit is less than 1"""
    if rate_limit < 1:
        raise ValueError("rate_limit must be at least 1")
    return rate_limit


class StreamingClient:
    """Talks to a (pretend) streaming-service API.

    What I promise:   the token never appears in repr(), str(), or error messages;
                      rate_limit is always >= 1; request_count only changes via fetch().
    What I expect:    callers use auth_header() -- the ONE place the token leaves this object.
    Who checks it?    Convention (underscore), the property setter, and tests.
                      NOT secured: vars(client) still shows _token.
    """

    def __init__(self, username: str, token: str, rate_limit: int = 10) -> None:
        self.username = username  # public on purpose: not a secret
        self._token = token
        self._rate_limit = _check(rate_limit)
        self._request_count = 0

    @property
    def rate_limit(self) -> int:
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, value: int) -> None:
        self._rate_limit = _check(value)

    @property
    def request_count(self) -> int:
        return self._request_count

    def auth_header(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self._token}"}

    def fetch(self, path: str) -> str:
        if self._request_count >= self._rate_limit:
            raise RuntimeError(f"rate limit of {self._rate_limit} reached for {path}")
        self._request_count += 1
        return f"pretend response for {path}"

    def __repr__(self) -> str:
        return f"StreamingClient(username={self.username!r}, token='***')"
