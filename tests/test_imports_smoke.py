from __future__ import annotations

import importlib
import types
import pytest


@pytest.mark.parametrize(
    "module_path",
    [
        "lichess_sdk",
        "lichess_sdk.create_request",
        "lichess_sdk.download_games",
        "lichess_sdk.types",
        "lichess_sdk.utils",
    ],
)
def test_module_imports(module_path: str) -> None:
    mod = importlib.import_module(module_path)
    assert isinstance(mod, types.ModuleType)
    assert mod.__name__ == module_path

