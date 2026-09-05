# Versioned API Routes

## Owns

HTTP routers for public, versioned platform API endpoints.

## Put here

Small route modules grouped by capability, such as `courses.py` and
`health.py`. Keep validation and response shapes explicit.

## Do not put here

Database queries, frontend code, or product-only business workflows. Delegate
shared business behavior to `services/` and persistence to `db/` or `models/`.

## Stop here

A route should translate HTTP input into a service call and return the API
contract. Do not place deep business logic in the router.
