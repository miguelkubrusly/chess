from __future__ import annotations

 
import json

from .create_request import create_request
from .utils import get_lichess_token
from .types import NdjsonGame, DownloadParams, PerfType
from .client import LichessClient
from lichess_org_api_reference_client.models.api_games_user_color import ApiGamesUserColor
from lichess_org_api_reference_client.models.api_games_user_sort import ApiGamesUserSort


def download_games(
    username: str,
    *,
    # Windowing and sizing
    max: int | None = None,
    since: int | None = None,  # epoch ms
    until: int | None = None,  # epoch ms
    # Filters
    rated: bool | None = None,
    perf_type: PerfType | None = None,  # bullet|blitz|rapid|classical|...
    color: ApiGamesUserColor | None = None,  # white|black
    vs: str | None = None,  # opponent username
    analysed: bool | None = None,
    ongoing: bool | None = None,
    finished: bool | None = None,
    sort: ApiGamesUserSort | None = None,  # dateDesc|dateAsc
    # Toggles for fields
    moves: bool | None = None,
    tags: bool | None = None,
    clocks: bool | None = None,
    evals: bool | None = None,
    opening: bool | None = None,
    accuracy: bool | None = None,  # requires analysed=True
    last_fen: bool | None = None,  # NDJSON only
    # Output
    format: str = "ndjson",  # "ndjson" (recommended) or "pgn"
    token: str | None = None,  # Lichess API token (optional for public)
    timeout: tuple[float | int, float | int] = (5, 30),
    client: LichessClient | None = None,
) -> list[NdjsonGame] | str:
    """Download games of a Lichess user.

    - Default returns NDJSON parsed into a list of dicts (recommended for processing).
    - Set format="pgn" to get a PGN string.
    - When requesting accuracy, ensure analysed=True.
    """
    if not username:
        raise ValueError("username is required")

    fmt = format.lower()
    if fmt not in {"ndjson", "pgn"}:
        raise ValueError("format must be 'ndjson' or 'pgn'")

    # Guard: lastFen is NDJSON-only. If PGN, drop it to avoid confusion.
    if fmt == "pgn" and last_fen:
        last_fen = None

    # Build query params using API's expected casing
    params: DownloadParams = {}
    param_mappings = {
        "max": max,
        "since": since,
        "until": until,
        "rated": rated,
        "perfType": perf_type,
        "color": color,
        "vs": vs,
        "analysed": analysed,
        "ongoing": ongoing,
        "finished": finished,
        "sort": sort,
        "moves": moves,
        "tags": tags,
        "clocks": clocks,
        "evals": evals,
        "opening": opening,
        "accuracy": accuracy,
        "lastFen": last_fen,
    }

    for key, value in param_mappings.items():
        if value is None:
            continue
        if key in [
            "rated",
            "analysed",
            "ongoing",
            "finished",
            "moves",
            "tags",
            "clocks",
            "evals",
            "opening",
            "accuracy",
            "lastFen",
        ]:
            params[key] = bool(value)
            continue
        if key in ["max", "since", "until"]:
            params[key] = int(value)
            continue
        if key == "color":
            params[key] = value.value  # type: ignore[assignment]
            continue
        if key == "sort":
            params[key] = value.value  # type: ignore[assignment]
            continue
        if key == "perfType":
            params[key] = value.value  # type: ignore[assignment]
            continue
        # Fallback: pass-through
        params[key] = value  # type: ignore[assignment]

    if accuracy and not analysed:
        # Warn early to prevent surprising empty accuracy fields
        raise ValueError("accuracy=True requires analysed=True")

    url = f"https://lichess.org/api/games/user/{username}"
    accept = "application/x-ndjson" if fmt == "ndjson" else "application/x-chess-pgn"

    bearer = token or get_lichess_token()

    resp = create_request(
        url,
        method="GET",
        accept=accept,
        api_key=bearer,
        use_bearer=True,
        client=client,
        params=params,  # type: ignore[arg-type]
        timeout=timeout,
        stream=True,
        # Align with docs: after 429, wait ~60s before retrying
        retries=2,
        backoff_factor=60,
    )

    if resp is None:
        raise RuntimeError("Request failed or no response returned")

    # Raise explicit error for non-2xx
    try:
        resp.raise_for_status()
    except Exception as e:
        body = None
        try:
            body = resp.text[:500]
        except Exception:
            pass
        raise RuntimeError(f"HTTP {resp.status_code}: {e}. Body: {body}")

    if fmt == "pgn":
        return resp.text

    # NDJSON: parse each line to JSON object
    games: list[NdjsonGame] = []
    for line in resp.iter_lines(decode_unicode=True):
        if not line:
            continue
        line = line.strip()
        if not line:
            continue
        obj: NdjsonGame = json.loads(line)
        games.append(obj)
    return games
