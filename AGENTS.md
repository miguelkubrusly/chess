# Repository Guidelines

## Project Structure & Module Organization
- `lichess_sdk/`: Core SDK (client, helpers, types). Public API re-exported in `__init__.py` for ergonomic imports.
- `tests/`: Pytest suites (e.g., `test_*.py`, `conftest.py`).
- `tools/openapi/`: OpenAPI spec, config, and generation utilities.
- `third_party/lichess_org_api_reference_client/`: Generated client (vendored). Do not edit by hand.
- `.env.example`: Sample environment variables (e.g., `LICHESS_API_TOKEN`).
- `Makefile`: Tasks for generating/cleaning the vendored client.

## Build, Test, and Development Commands
- `pytest -q`: Run tests.
- `ruff check .` / `ruff format .`: Lint and format code (Ruff defaults).
- `mypy lichess_sdk`: Type-check SDK code (Python 3.11).
- `make gen-client`: Regenerate the OpenAPI client into `third_party/…`.
- `make clean-client`: Remove generated artifacts.

Example: run full local check

```
pytest -q && ruff check . && mypy lichess_sdk
```

## Coding Style & Naming Conventions
- Python 3.11, 4-space indentation, PEP 8, type hints required in new/changed code.
- Modules: `snake_case.py`; classes: `PascalCase`; functions/vars: `snake_case`.
- Keep the public surface via `lichess_sdk/__init__.py` stable; prefer internal helpers in module files.
- Use docstrings for public functions/classes; keep imports explicit and local to call sites when practical.

## Testing Guidelines
- Framework: Pytest. Place tests under `tests/` with files named `test_*.py`.
- Prefer parametrized tests (`@pytest.mark.parametrize`) and small, focused assertions.
- Run `pytest -q` locally before opening a PR. Add coverage for new branches and error paths when touching logic.

## Commit & Pull Request Guidelines
- Commits: short, imperative subject lines (e.g., `sdk: add download helper`, `tests: parametrize imports`).
- Group changes logically; avoid mixing refactors with feature changes.
- PRs must include: clear description, rationale, screenshots or CLI output when relevant, and test coverage for changes.
- Link related issues. Ensure CI-equivalent: `pytest`, `ruff check`, and `mypy` pass.

## Security & Configuration Tips
- Configure `LICHESS_API_TOKEN` in `.env` (never commit secrets). Load via standard tooling if needed.
- Do not edit `third_party/…` manually; regenerate via `make gen-client` to pick up spec changes.
