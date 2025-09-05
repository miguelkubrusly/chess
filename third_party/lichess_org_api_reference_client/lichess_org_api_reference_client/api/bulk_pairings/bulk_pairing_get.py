from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_pairing_get_response_200 import BulkPairingGetResponse200
from ...models.bulk_pairing_get_response_404 import BulkPairingGetResponse404
from typing import cast



def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/bulk-pairing/{id}".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]:
    if response.status_code == 200:
        response_200 = BulkPairingGetResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = BulkPairingGetResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]:
    """ Show a bulk pairing

     Get a single bulk pairing by its ID.

    Args:
        id (str): The ID of the bulk pairing Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]:
    """ Show a bulk pairing

     Get a single bulk pairing by its ID.

    Args:
        id (str): The ID of the bulk pairing Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkPairingGetResponse200, BulkPairingGetResponse404]
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]:
    """ Show a bulk pairing

     Get a single bulk pairing by its ID.

    Args:
        id (str): The ID of the bulk pairing Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Optional[Union[BulkPairingGetResponse200, BulkPairingGetResponse404]]:
    """ Show a bulk pairing

     Get a single bulk pairing by its ID.

    Args:
        id (str): The ID of the bulk pairing Example: 5IrD6Gzz.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkPairingGetResponse200, BulkPairingGetResponse404]
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
