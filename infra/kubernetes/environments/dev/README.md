# Development Environment

## Owns

The development environment entrypoint. It aggregates approved `dev` overlays
for applications deployed to the development cluster or namespace.

## Put here

Environment-level Kustomizations, ordering, and development-only composition.

## Do not put here

Reusable application defaults or source code. Those belong in an app `base` or
the application repository.

## Stop here

Change this directory only when the set or composition of development
workloads changes.