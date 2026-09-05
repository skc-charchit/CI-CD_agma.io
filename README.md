# CI-CD_agma.io

This repository is the shared company-platform repository. It owns the public
company website, shared platform API, reusable packages, deployment manifests,
and starter templates. Independent products live in their own repositories.

## Owns

The repository-level architecture, shared platform boundaries, and navigation
to each owned application area.

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

## Product boundary

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

The company website links each product card to that product's own route or
domain. A product can begin at
`company.example/products/product-name` and later move to
`product-name.example` without changing the product ownership boundary.

## Agent rules

- Put company website code in `apps/company-web`.
- Put shared server-side behavior in `apps/api`.
- Put reusable code used by multiple apps in `packages`.
- Put deployment and environment configuration in `infra`.
- Put new-product starting points in `templates`; do not run code directly from
	a template.
- Stop at the owning boundary. Do not add product-specific business logic to
	the company website, shared API, or templates.

## Local development

See [docs/architecture.md](docs/architecture.md) for the complete request flow,
folder responsibilities, local startup steps, and review process.

Start both local services with:

```bash
./scripts/dev.sh
```

Open `http://127.0.0.1:5500` for the company website. Run the review checks
before pushing with:

```bash
./scripts/check.sh
```