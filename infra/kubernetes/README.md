# Kubernetes Structure

## Owns

Kubernetes manifests for the API, company website, platform services, and
product deployments. Manifests are organized with Kustomize.

```text
kubernetes/
├── apps/
│   ├── api/
│   │   ├── base/
│   │   └── overlays/{dev,staging,production}/
│   ├── company-web/
│   │   ├── base/
│   │   └── overlays/{dev,staging,production}/
│   └── products/              Product deployment manifests from separate repos
│       └── _template/
├── cluster/
│   └── platform/        Ingress, cert-manager, monitoring, and controllers
├── environments/
│   ├── dev/
│   ├── staging/
│   └── production/      Environment entry points for GitOps tools
├── namespaces/          Namespace definitions and resource quotas
└── policies/            Network policies, pod security, and policy rules
```

## Rules

- `base/` contains environment-independent manifests only.
- `overlays/` contains environment-specific images, replicas, domains, and resources.
- Secrets are stored in a secret manager or encrypted with a tool such as SOPS; never commit plaintext secrets.
- Each product gets its own directory under `products/` using `_template` as the starting point.
- Product workloads should use separate namespaces or clearly defined labels and resource ownership.
- CI builds and publishes images; deployment automation applies the selected overlay.
- Cluster-wide infrastructure belongs in `cluster/`, not inside an application directory.

## Stop here

Keep application runtime code outside this directory. Put shared Kubernetes
defaults in `base/`, environment differences in an overlay, and product
deployment resources under `products/`.

The production application overlays currently target the `agma-production`
namespace. Replace the example ingress host in the company-web production
overlay before deploying.