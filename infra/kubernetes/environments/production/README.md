# Production Environment

## Owns

The production environment entrypoint. It aggregates approved `production`
overlays for applications deployed to the production cluster or namespace.

## Put here

Environment-level Kustomizations, ordering, and production-only composition.

## Do not put here

Reusable application defaults, plaintext secrets, or source code. Production
changes must use the approved secret and deployment workflows.

## Stop here

Change this directory only when the production workload composition changes.
Production changes require review and an approved deployment workflow.