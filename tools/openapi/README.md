# OpenAPI Specs and Generation

This folder organizes the official Lichess OpenAPI materials and config used to
generate the reference Python client.

Structure
- `specs/`: Official OpenAPI YAML files (copied from `lichess_oficial_docs`).
- `config/`: Client generator configuration.
- `examples/`: Example apps/snippets (JS/TS) demonstrating OAuth flows.

Suggested generation (outside this sandbox)

    openapi-python-client generate \
      --path tools/openapi/specs/lichess-api.yaml \
      --config tools/openapi/config/client_config.yaml \
      --overwrite

Output can be installed as a dependency or vendored into
`third_party/lichess_org_api_reference_client/` if needed.

