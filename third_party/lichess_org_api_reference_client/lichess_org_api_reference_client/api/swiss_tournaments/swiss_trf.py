from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/swiss/{id}.trf".format(id=id,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[str]:
    if response.status_code == 200:
        response_200 = response.text
        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[str]:
    """ Export TRF of a Swiss tournament

     Download a tournament in the Tournament Report File format, the FIDE standard.
    Documentation: <https://www.fide.com/FIDE/handbook/C04Annex2_TRF16.pdf>
    Example: <https://lichess.org/swiss/j8rtJ5GL.trf>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[str]:
    """ Export TRF of a Swiss tournament

     Download a tournament in the Tournament Report File format, the FIDE standard.
    Documentation: <https://www.fide.com/FIDE/handbook/C04Annex2_TRF16.pdf>
    Example: <https://lichess.org/swiss/j8rtJ5GL.trf>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[str]:
    """ Export TRF of a Swiss tournament

     Download a tournament in the Tournament Report File format, the FIDE standard.
    Documentation: <https://www.fide.com/FIDE/handbook/C04Annex2_TRF16.pdf>
    Example: <https://lichess.org/swiss/j8rtJ5GL.trf>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[str]
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
    client: Union[AuthenticatedClient, Client],

) -> Optional[str]:
    """ Export TRF of a Swiss tournament

     Download a tournament in the Tournament Report File format, the FIDE standard.
    Documentation: <https://www.fide.com/FIDE/handbook/C04Annex2_TRF16.pdf>
    Example: <https://lichess.org/swiss/j8rtJ5GL.trf>

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        str
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
