# Platform Services

## Owns

Cluster-wide services required by multiple workloads, such as ingress, TLS
management, external DNS, observability, autoscaling controllers, and policy
controllers.

## Do not put here

Application deployments, product services, application namespaces, or
environment-specific replicas and domains.

## Stop here

If a manifest serves one application, move it to `kubernetes/apps/`. If it
serves one product, use `kubernetes/products/`.