from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.write_note_body import WriteNoteBody
from ...models.write_note_response_200 import WriteNoteResponse200
from typing import cast



def _get_kwargs(
    username: str,
    *,
    body: WriteNoteBody,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/user/{username}/note".format(username=username,),
    }

    _kwargs["data"] = body.to_dict()

    headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[WriteNoteResponse200]:
    if response.status_code == 200:
        response_200 = WriteNoteResponse200.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[WriteNoteResponse200]:
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
    body: WriteNoteBody,

) -> Response[WriteNoteResponse200]:
    """ Add a note for a user

     Add a private note available only to you about this account.

    Args:
        username (str):  Example: thibault.
        body (WriteNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WriteNoteResponse200]
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
    body: WriteNoteBody,

) -> Optional[WriteNoteResponse200]:
    """ Add a note for a user

     Add a private note available only to you about this account.

    Args:
        username (str):  Example: thibault.
        body (WriteNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WriteNoteResponse200
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
    body: WriteNoteBody,

) -> Response[WriteNoteResponse200]:
    """ Add a note for a user

     Add a private note available only to you about this account.

    Args:
        username (str):  Example: thibault.
        body (WriteNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[WriteNoteResponse200]
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
    body: WriteNoteBody,

) -> Optional[WriteNoteResponse200]:
    """ Add a note for a user

     Add a private note available only to you about this account.

    Args:
        username (str):  Example: thibault.
        body (WriteNoteBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        WriteNoteResponse200
     """


    return (await asyncio_detailed(
        username=username,
client=client,
body=body,

    )).parsed
