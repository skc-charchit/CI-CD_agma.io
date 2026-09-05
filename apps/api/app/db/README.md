# API Database Layer

## Owns

Database sessions, connections, migrations, and persistence infrastructure for
shared platform data.

## Do not put here

HTTP routes, response formatting, frontend code, or product-specific database
schemas.

## Stop here

Keep this layer responsible for persistence mechanics. Business decisions
belong in `services/`.
