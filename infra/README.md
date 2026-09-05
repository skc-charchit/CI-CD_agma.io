# Infrastructure

## Owns

Deployment, hosting, containers, cluster configuration, and environment
configuration for platform applications and products.

## Folders

- `kubernetes/`: Kubernetes manifests organized with Kustomize.
- `terraform/`: Cloud infrastructure, networking, databases, and managed
	services when introduced.
- `helm/`: Reusable Helm charts only when chart packaging is required.

## Do not put here

Application source code, frontend assets, business logic, or plaintext secrets.

## Stop here

Infrastructure describes how software runs. Make code changes in `apps` or
`packages`, then update deployment configuration only when runtime needs change.