#!/usr/bin/env python3
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOLS = ROOT / "tools" / "openapi"
SPEC = TOOLS / "specs" / "lichess-api.yaml"
CONFIG = TOOLS / "config" / "client_config.yaml"
BUILD_DIR = ROOT / ".openapi_client_build"
OUT_PROJECT = BUILD_DIR / "lichess-org-api-reference-client"
SRC_PKG = OUT_PROJECT / "lichess_org_api_reference_client"
DEST_PKG = ROOT / "third_party" / "lichess_org_api_reference_client"


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def main() -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    # Generate into BUILD_DIR
    run([
        "openapi-python-client",
        "generate",
        "--path",
        str(SPEC),
        "--config",
        str(CONFIG),
        "--output-dir",
        str(BUILD_DIR),
        "--overwrite",
    ])

    if not SRC_PKG.exists():
        raise SystemExit(f"Expected generated package at {SRC_PKG}, but it was not found.")

    DEST_PKG.parent.mkdir(parents=True, exist_ok=True)
    if DEST_PKG.exists():
        shutil.rmtree(DEST_PKG)
    shutil.copytree(SRC_PKG, DEST_PKG)
    print(f"Vendored client updated at {DEST_PKG}")


if __name__ == "__main__":
    main()

