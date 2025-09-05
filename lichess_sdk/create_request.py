"""HTTP helper with retries and sensible defaults for Lichess API."""

from typing import Any, Callable
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .utils import get_api_key, get_lichess_token
from .client import LichessClient
from .types import HTTPMethod


def create_request(
    url: str,
    method: HTTPMethod | str = "GET",
    *,
    content_type: str = "application/json",
    accept: str = "application/json",
    api_key: str | None = None,
    use_bearer: bool = False,
    client: LichessClient | None = None,
    payload_func: Callable[..., Any] | None = None,
    json: object | None = None,
    data: object | None = None,
    params: dict[str, str] | None = None,
    extra_headers: dict[str, str] | None = None,
    timeout: tuple[int | float, int | float] = (5, 15),
    retries: int = 2,
    backoff_factor: float = 0.5,
    retry_statuses: tuple[int, ...] = (429, 500, 502, 503, 504),
    stream: bool = False,
    respect_retry_after_header: bool = True,
) -> requests.Response | None:
    """Send an HTTP request with standard headers and resiliency options."""
    # Resolve token/key when needed. For Lichess, Bearer token is optional for public data.
    if api_key is None and use_bearer:
        api_key = get_lichess_token()

    # Base headers from optional client, otherwise minimal defaults
    if client is not None:
        headers = client.get_headers(accept=accept, content_type=content_type, include_auth=True)
    else:
        headers = {
            "Accept": accept,
            "Content-Type": content_type,
        }

    # Attach/override auth header if provided
    if api_key:
        if use_bearer:
            headers["Authorization"] = f"Bearer {api_key}"
        else:
            headers["X-API-KEY"] = api_key
    if extra_headers:
        headers.update(extra_headers)

    if payload_func and json is None and data is None:
        try:
            generated = payload_func()
            if content_type == "application/json":
                json = generated
            else:
                data = generated
        except Exception as e:
            print(f"Erro ao gerar payload: {e}")
            return None

    session = requests.Session()
    retry = Retry(
        total=retries,
        connect=retries,
        read=retries,
        status=retries,
        backoff_factor=backoff_factor,
        status_forcelist=retry_statuses,
        allowed_methods={"GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"},
        raise_on_status=False,
        respect_retry_after_header=respect_retry_after_header,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)

    try:
        response: requests.Response = session.request(
            method=method.upper(),
            url=url,
            headers=headers,
            params=params,
            json=json,
            data=data,
            timeout=timeout,
            stream=stream,
        )
        return response
    except requests.exceptions.Timeout:
        print("The request timed out")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

