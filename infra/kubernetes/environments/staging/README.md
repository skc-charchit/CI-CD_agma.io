# Staging Environment

## Owns

The staging environment entrypoint. It aggregates approved `staging` overlays
for applications deployed to the staging cluster or namespace.

## Put here

Environment-level Kustomizations, ordering, and staging-only composition.

## Do not put here

Reusable application defaults, secrets, or source code. Those belong in an app
`base`, a secret manager, or the application repository.

## Stop here

Change this directory only when the set or composition of staging workloads
changes.