from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping


DEFAULT_BASE_URL = "https://lichess.org"


@dataclass(slots=True)
class LichessClient:
    """Minimal HTTP client config for Lichess API.

    This is a thin configuration holder. It does not perform HTTP by itself;
    use it with helpers like `create_request` to issue requests with defaults.
    """

    base_url: str = DEFAULT_BASE_URL
    token: str | None = None
    user_agent: str | None = "lichess-sdk/0.2.0"
    extra_headers: Mapping[str, str] = field(default_factory=dict)

    def get_headers(
        self,
        *,
        accept: str = "application/json",
        content_type: str = "application/json",
        include_auth: bool = True,
    ) -> dict[str, str]:
        """Build default headers for Lichess API calls."""
        headers: dict[str, str] = {
            "Accept": accept,
            "Content-Type": content_type,
        }
        if self.user_agent:
            headers["User-Agent"] = self.user_agent
        if include_auth and self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if self.extra_headers:
            headers.update(self.extra_headers)
        return headers

