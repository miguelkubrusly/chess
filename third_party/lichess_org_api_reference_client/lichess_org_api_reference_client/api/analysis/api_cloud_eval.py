from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.api_cloud_eval_response_200 import ApiCloudEvalResponse200
from ...models.api_cloud_eval_response_404 import ApiCloudEvalResponse404
from ...models.api_cloud_eval_variant import ApiCloudEvalVariant
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    fen: str,
    multi_pv: Union[Unset, float] = 1.0,
    variant: Union[Unset, ApiCloudEvalVariant] = ApiCloudEvalVariant.STANDARD,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["fen"] = fen

    params["multiPv"] = multi_pv

    json_variant: Union[Unset, str] = UNSET
    if not isinstance(variant, Unset):
        json_variant = variant.value

    params["variant"] = json_variant


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/cloud-eval",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]:
    if response.status_code == 200:
        response_200 = ApiCloudEvalResponse200.from_dict(response.json())



        return response_200

    if response.status_code == 404:
        response_404 = ApiCloudEvalResponse404.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,
    multi_pv: Union[Unset, float] = 1.0,
    variant: Union[Unset, ApiCloudEvalVariant] = ApiCloudEvalVariant.STANDARD,

) -> Response[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]:
    """ Get cloud evaluation of a position.

     Get the cached evaluation of a position, if available.
    Opening positions have more chances of being available. There are about 15 million positions in the
    database.
    Up to 5 variations may be available. Variants are supported.
    Use this endpoint to fetch a few positions here and there.
    If you want to download a lot of positions, [get the full list](https://database.lichess.org/#evals)
    from our exported database.

    Args:
        fen (str):
        multi_pv (Union[Unset, float]):  Default: 1.0.
        variant (Union[Unset, ApiCloudEvalVariant]):  Default: ApiCloudEvalVariant.STANDARD.
            Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]
     """


    kwargs = _get_kwargs(
        fen=fen,
multi_pv=multi_pv,
variant=variant,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,
    multi_pv: Union[Unset, float] = 1.0,
    variant: Union[Unset, ApiCloudEvalVariant] = ApiCloudEvalVariant.STANDARD,

) -> Optional[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]:
    """ Get cloud evaluation of a position.

     Get the cached evaluation of a position, if available.
    Opening positions have more chances of being available. There are about 15 million positions in the
    database.
    Up to 5 variations may be available. Variants are supported.
    Use this endpoint to fetch a few positions here and there.
    If you want to download a lot of positions, [get the full list](https://database.lichess.org/#evals)
    from our exported database.

    Args:
        fen (str):
        multi_pv (Union[Unset, float]):  Default: 1.0.
        variant (Union[Unset, ApiCloudEvalVariant]):  Default: ApiCloudEvalVariant.STANDARD.
            Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]
     """


    return sync_detailed(
        client=client,
fen=fen,
multi_pv=multi_pv,
variant=variant,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,
    multi_pv: Union[Unset, float] = 1.0,
    variant: Union[Unset, ApiCloudEvalVariant] = ApiCloudEvalVariant.STANDARD,

) -> Response[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]:
    """ Get cloud evaluation of a position.

     Get the cached evaluation of a position, if available.
    Opening positions have more chances of being available. There are about 15 million positions in the
    database.
    Up to 5 variations may be available. Variants are supported.
    Use this endpoint to fetch a few positions here and there.
    If you want to download a lot of positions, [get the full list](https://database.lichess.org/#evals)
    from our exported database.

    Args:
        fen (str):
        multi_pv (Union[Unset, float]):  Default: 1.0.
        variant (Union[Unset, ApiCloudEvalVariant]):  Default: ApiCloudEvalVariant.STANDARD.
            Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]
     """


    kwargs = _get_kwargs(
        fen=fen,
multi_pv=multi_pv,
variant=variant,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    fen: str,
    multi_pv: Union[Unset, float] = 1.0,
    variant: Union[Unset, ApiCloudEvalVariant] = ApiCloudEvalVariant.STANDARD,

) -> Optional[Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]]:
    """ Get cloud evaluation of a position.

     Get the cached evaluation of a position, if available.
    Opening positions have more chances of being available. There are about 15 million positions in the
    database.
    Up to 5 variations may be available. Variants are supported.
    Use this endpoint to fetch a few positions here and there.
    If you want to download a lot of positions, [get the full list](https://database.lichess.org/#evals)
    from our exported database.

    Args:
        fen (str):
        multi_pv (Union[Unset, float]):  Default: 1.0.
        variant (Union[Unset, ApiCloudEvalVariant]):  Default: ApiCloudEvalVariant.STANDARD.
            Example: standard.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApiCloudEvalResponse200, ApiCloudEvalResponse404]
     """


    return (await asyncio_detailed(
        client=client,
fen=fen,
multi_pv=multi_pv,
variant=variant,

    )).parsed
