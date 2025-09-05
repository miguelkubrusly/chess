from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.inbox_username_body import InboxUsernameBody
from ...models.inbox_username_response_200 import InboxUsernameResponse200
from ...models.inbox_username_response_400 import InboxUsernameResponse400
from typing import cast



def _get_kwargs(
    username: str,
    *,
    body: InboxUsernameBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/inbox/{username}".format(username=username,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[InboxUsernameResponse200, InboxUsernameResponse400]]:
    if response.status_code == 200:
        response_200 = InboxUsernameResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = InboxUsernameResponse400.from_dict(response.json())



        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[InboxUsernameResponse200, InboxUsernameResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: InboxUsernameBody,

) -> Response[Union[InboxUsernameResponse200, InboxUsernameResponse400]]:
    """ Send a private message

     Send a private message to another player.

    Args:
        username (str):  Example: someplayer.
        body (InboxUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InboxUsernameResponse200, InboxUsernameResponse400]]
     """


    kwargs = _get_kwargs(
        username=username,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    username: str,
    *,
    client: AuthenticatedClient,
    body: InboxUsernameBody,

) -> Optional[Union[InboxUsernameResponse200, InboxUsernameResponse400]]:
    """ Send a private message

     Send a private message to another player.

    Args:
        username (str):  Example: someplayer.
        body (InboxUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InboxUsernameResponse200, InboxUsernameResponse400]
     """


    return sync_detailed(
        username=username,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
    body: InboxUsernameBody,

) -> Response[Union[InboxUsernameResponse200, InboxUsernameResponse400]]:
    """ Send a private message

     Send a private message to another player.

    Args:
        username (str):  Example: someplayer.
        body (InboxUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[InboxUsernameResponse200, InboxUsernameResponse400]]
     """


    kwargs = _get_kwargs(
        username=username,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
    body: InboxUsernameBody,

) -> Optional[Union[InboxUsernameResponse200, InboxUsernameResponse400]]:
    """ Send a private message

     Send a private message to another player.

    Args:
        username (str):  Example: someplayer.
        body (InboxUsernameBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[InboxUsernameResponse200, InboxUsernameResponse400]
     """


    return (await asyncio_detailed(
        username=username,
client=client,
body=body,

    )).parsed
