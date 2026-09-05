# Shared Configuration

## Owns

Shared linting, formatting, type-checking, and build configuration used by more
than one application.

## Put here

Reusable tool configuration and documented defaults that can be consumed by
the company website, API, or product repositories.

## Do not put here

Application-specific settings, secrets, environment values, or deployment
overlays. Those belong with the application or under `infra`.

## Stop here

Only add configuration when at least two consumers need the same rule. Keep
one-off settings in the owning application.