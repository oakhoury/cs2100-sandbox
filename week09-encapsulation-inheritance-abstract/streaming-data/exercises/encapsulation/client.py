"""Encapsultion (intentionally flawed). Students fix this file.

    pytest exercises/encapsulation        # see which promises it breaks and fix them!
"""


class StreamingClient:
    """Talks to a (pretend) streaming-service API.

    What I promise:   the token never appears in repr(), str(), or error messages;
                      rate_limit is always >= 1; 
                      request_count only changes via fetch().
    What I expect:    callers use auth_header() -- the ONE place the token leaves this object,
                        as it's needed for the authenticatation with the streaming service
    Who checks it?    Convention (underscore), the property setter, and tests.

    """

    def __init__(self, username: str, token: str, rate_limit: int = 10) -> None:
        self.username = username
        self.token = token
        self.rate_limit = rate_limit
        self.request_count = 0

    @property
    def rate_limit(self) -> int:
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, value: int) -> None:
        self._rate_limit = value

    def auth_header(self) -> dict[str, str]:
        return {"Authorization": f"Bearer {self.token}"}

    def fetch(self, path: str) -> str:
        if self.request_count >= self.rate_limit:
            raise RuntimeError(f"rate limit hit for {path}")
        self.request_count += 1
        return f"pretend response for {path}"

    def __repr__(self) -> str:
        # Handy while debugging... and a classic way secrets end up in log files.
        return f"StreamingClient(username={self.username!r}, token={self.token!r})"
