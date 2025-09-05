from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_user_perf_perf import ApiUserPerfPerf



def _get_kwargs(
    username: str,
    perf: ApiUserPerfPerf,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/user/{username}/perf/{perf}".format(username=username,perf=perf,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    perf: ApiUserPerfPerf,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Get performance statistics of a user

     Read performance statistics of a user, for a single performance.
    Similar to the [performance pages on the website](https://lichess.org/@/thibault/perf/bullet).

    Args:
        username (str):
        perf (ApiUserPerfPerf):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
perf=perf,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    username: str,
    perf: ApiUserPerfPerf,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Get performance statistics of a user

     Read performance statistics of a user, for a single performance.
    Similar to the [performance pages on the website](https://lichess.org/@/thibault/perf/bullet).

    Args:
        username (str):
        perf (ApiUserPerfPerf):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        username=username,
perf=perf,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

