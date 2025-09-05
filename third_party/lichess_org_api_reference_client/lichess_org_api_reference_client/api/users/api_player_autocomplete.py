from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_player_autocomplete_response_200_type_1 import ApiPlayerAutocompleteResponse200Type1
from ...types import UNSET, Unset
from typing import cast
from typing import cast, Union
from typing import Union



def _get_kwargs(
    *,
    term: str,
    object_: Union[Unset, bool] = False,
    names: Union[Unset, bool] = False,
    friend: Union[Unset, bool] = UNSET,
    team: Union[Unset, str] = UNSET,
    tour: Union[Unset, str] = UNSET,
    swiss: Union[Unset, str] = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["term"] = term

    params["object"] = object_

    params["names"] = names

    params["friend"] = friend

    params["team"] = team

    params["tour"] = tour

    params["swiss"] = swiss


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/player/autocomplete",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]:
    if response.status_code == 200:
        def _parse_response_200(data: object) -> Union['ApiPlayerAutocompleteResponse200Type1', list[str]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                response_200_type_0 = cast(list[str], data)

                return response_200_type_0
            except: # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = ApiPlayerAutocompleteResponse200Type1.from_dict(data)



            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    object_: Union[Unset, bool] = False,
    names: Union[Unset, bool] = False,
    friend: Union[Unset, bool] = UNSET,
    team: Union[Unset, str] = UNSET,
    tour: Union[Unset, str] = UNSET,
    swiss: Union[Unset, str] = UNSET,

) -> Response[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]:
    """ Autocomplete usernames

     Provides autocompletion options for an incomplete username.

    Args:
        term (str):
        object_ (Union[Unset, bool]):  Default: False.
        names (Union[Unset, bool]):  Default: False.
        friend (Union[Unset, bool]):
        team (Union[Unset, str]):
        tour (Union[Unset, str]):
        swiss (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]
     """


    kwargs = _get_kwargs(
        term=term,
object_=object_,
names=names,
friend=friend,
team=team,
tour=tour,
swiss=swiss,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    object_: Union[Unset, bool] = False,
    names: Union[Unset, bool] = False,
    friend: Union[Unset, bool] = UNSET,
    team: Union[Unset, str] = UNSET,
    tour: Union[Unset, str] = UNSET,
    swiss: Union[Unset, str] = UNSET,

) -> Optional[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]:
    """ Autocomplete usernames

     Provides autocompletion options for an incomplete username.

    Args:
        term (str):
        object_ (Union[Unset, bool]):  Default: False.
        names (Union[Unset, bool]):  Default: False.
        friend (Union[Unset, bool]):
        team (Union[Unset, str]):
        tour (Union[Unset, str]):
        swiss (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ApiPlayerAutocompleteResponse200Type1', list[str]]
     """


    return sync_detailed(
        client=client,
term=term,
object_=object_,
names=names,
friend=friend,
team=team,
tour=tour,
swiss=swiss,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    object_: Union[Unset, bool] = False,
    names: Union[Unset, bool] = False,
    friend: Union[Unset, bool] = UNSET,
    team: Union[Unset, str] = UNSET,
    tour: Union[Unset, str] = UNSET,
    swiss: Union[Unset, str] = UNSET,

) -> Response[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]:
    """ Autocomplete usernames

     Provides autocompletion options for an incomplete username.

    Args:
        term (str):
        object_ (Union[Unset, bool]):  Default: False.
        names (Union[Unset, bool]):  Default: False.
        friend (Union[Unset, bool]):
        team (Union[Unset, str]):
        tour (Union[Unset, str]):
        swiss (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]
     """


    kwargs = _get_kwargs(
        term=term,
object_=object_,
names=names,
friend=friend,
team=team,
tour=tour,
swiss=swiss,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    object_: Union[Unset, bool] = False,
    names: Union[Unset, bool] = False,
    friend: Union[Unset, bool] = UNSET,
    team: Union[Unset, str] = UNSET,
    tour: Union[Unset, str] = UNSET,
    swiss: Union[Unset, str] = UNSET,

) -> Optional[Union['ApiPlayerAutocompleteResponse200Type1', list[str]]]:
    """ Autocomplete usernames

     Provides autocompletion options for an incomplete username.

    Args:
        term (str):
        object_ (Union[Unset, bool]):  Default: False.
        names (Union[Unset, bool]):  Default: False.
        friend (Union[Unset, bool]):
        team (Union[Unset, str]):
        tour (Union[Unset, str]):
        swiss (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union['ApiPlayerAutocompleteResponse200Type1', list[str]]
     """


    return (await asyncio_detailed(
        client=client,
term=term,
object_=object_,
names=names,
friend=friend,
team=team,
tour=tour,
swiss=swiss,

    )).parsed
