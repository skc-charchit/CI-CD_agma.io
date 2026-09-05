# Product Template

## Owns

This directory is a starting point for a new, independent product repository.
It is not a running company website or shared application.

## Use it this way

Copy the directory into a new product repository. Keep browser code in
`frontend/`, product server code in `backend/`, and product deployment
manifests in the central `infra/kubernetes/products/<product-name>/` location.
Consume shared packages from this platform repository.

## Do not put here

Live company homepage code, shared API routes, secrets, or environment-specific
deployment manifests.

## Stop here

After copying the template, product ownership begins in the new repository.
Changes to shared platform behavior must return to `apps/api`, `packages`, or
the central `infra` directories.