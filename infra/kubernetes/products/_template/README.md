# Product Kubernetes Template

## Owns

The starter deployment structure for a product whose source code lives in a
separate repository.

## Use it this way

Copy this directory to `infra/kubernetes/products/<product-name>/`. Put
environment-independent workload manifests in `base/`, then create
`overlays/dev`, `overlays/staging`, and `overlays/production` for environment-
specific settings.

## Do not put here

Product source code, company-wide application deployments, or plaintext
secrets.

## Stop here

Keep this directory limited to deployment resources for one product. Shared
cluster services belong in `cluster/`, and shared application manifests belong
under `apps/`.