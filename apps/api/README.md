# Platform API

## Owns

This service owns shared server-side capabilities and versioned APIs used by
the company website and product applications. The Python package lives in
`app/`.

## Put here

- HTTP routers under `app/api/v1/`.
- Request and response contracts under `app/schemas/`.
- Shared business services under `app/services/`.
- Shared persistence code under `app/db/` and `app/models/`.
- Runtime configuration under `app/config.py`.

## Do not put here

Browser UI, HTML, CSS, product-specific business rules, or product-specific
databases. Those belong in `apps/company-web` or the relevant product
repository.

## Stop here

Add a route here only when it is a shared platform capability. Stop at the API
contract; do not build frontend components in this directory.

Run the API locally from the repository root with:

```bash
PYTHONPATH=apps/api uv run uvicorn app.main:app --reload --port 8000
```