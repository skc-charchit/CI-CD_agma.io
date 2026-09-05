# CI-CD_agma.io

This repository is the shared company-platform repository in a mixed-repository
architecture. Company-wide applications and shared infrastructure stay here;
each independent product can live in its own repository.

## Repository layout

```text
CI-CD_agma.io/                  Shared platform repository
├── apps/
│   ├── company-web/            Company website and product catalog
│   └── api/                    Shared Python platform API
├── packages/
│   ├── ui/                     Shared frontend components
│   ├── types/                  Shared API contracts
│   └── config/                 Shared tooling configuration
├── infra/
│   ├── kubernetes/             Platform and product deployment manifests
│   ├── terraform/              Cloud infrastructure (future)
│   └── helm/                   Reusable charts (future)
├── templates/
│   └── product/                Starter structure for new product repositories
├── docs/                       Architecture and product documentation
└── scripts/                    Repository automation
```

Product source repositories are separate:

```text
product-analytics/
product-payments/
product-crm/
```

Kubernetes manifests live under `infra/kubernetes`. Each deployable application
has a reusable `base` and environment overlays for `dev`, `staging`, and
`production`. Product deployment manifests are maintained centrally under
`infra/kubernetes/products/<product-name>`.

The company website should link each product card to that product's own route or
domain. For example, a product can begin at
`company.example/products/product-name` and later move to
`product-name.example` without changing the product ownership boundary.