from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.account_kid_post_response_200 import AccountKidPostResponse200
from typing import cast



def _get_kwargs(
    *,
    v: bool,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["v"] = v


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/account/kid",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[AccountKidPostResponse200]:
    if response.status_code == 200:
        response_200 = AccountKidPostResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[AccountKidPostResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    v: bool,

) -> Response[AccountKidPostResponse200]:
    """ Set my kid mode status

     Set the kid mode status of the logged in user.
    - <https://lichess.org/account/kid>

    Args:
        v (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountKidPostResponse200]
     """


    kwargs = _get_kwargs(
        v=v,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    v: bool,

) -> Optional[AccountKidPostResponse200]:
    """ Set my kid mode status

     Set the kid mode status of the logged in user.
    - <https://lichess.org/account/kid>

    Args:
        v (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountKidPostResponse200
     """


    return sync_detailed(
        client=client,
v=v,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    v: bool,

) -> Response[AccountKidPostResponse200]:
    """ Set my kid mode status

     Set the kid mode status of the logged in user.
    - <https://lichess.org/account/kid>

    Args:
        v (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountKidPostResponse200]
     """


    kwargs = _get_kwargs(
        v=v,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    v: bool,

) -> Optional[AccountKidPostResponse200]:
    """ Set my kid mode status

     Set the kid mode status of the logged in user.
    - <https://lichess.org/account/kid>

    Args:
        v (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountKidPostResponse200
     """


    return (await asyncio_detailed(
        client=client,
v=v,

    )).parsed
