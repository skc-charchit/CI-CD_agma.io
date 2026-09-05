# Namespaces

## Owns

Application namespaces, resource quotas, limit ranges, and namespace-level
defaults.

## Do not put here

Deployments, services, ingress rules, application code, or secrets.

## Stop here

Only add resources that apply to a namespace boundary. Workload-specific
resources belong under `apps/` or `products/`.