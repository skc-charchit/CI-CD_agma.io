# Frontend and Backend Boundaries

## Repository responsibilities

```text
apps/
├── company-web/       Frontend: company pages and product catalog
└── api/               Backend: shared platform API

Separate repositories:
├── product-analytics/  Product frontend and backend
├── product-payments/  Product frontend and backend
└── product-crm/       Product frontend and backend
```

### Frontend

Frontend code runs in the browser and belongs in:

- `apps/company-web/src`: company website pages and components.
- `apps/company-web/public`: static website assets.
- `<product-repository>/frontend`: product-specific UI.
- `packages/ui`: reusable UI components.

Frontend responsibilities include pages, navigation, forms, client-side state,
API calls, and user-facing assets.

### Backend

Backend code runs on servers and belongs in:

- `apps/api/app`: shared APIs, authentication, platform services, and shared data access.
- `<product-repository>/backend`: product-specific APIs, business rules, and data access.

Backend responsibilities include authentication, authorization, business rules,
database access, background jobs, integrations, and API responses.

### Shared code

Code used by more than one application belongs in `packages/`, not in either a
frontend or backend application:

- `packages/ui`: shared frontend components and design system.
- `packages/types`: shared API contracts and data types.
- `packages/config`: shared tooling configuration.

## Product example

```text
product-analytics/
├── frontend/
│   ├── src/
│   └── public/
├── backend/
│   └── app/
├── tests/
└── README.md
```

The company website links to the product. The product frontend calls the
product backend, and the product backend can call the shared `apps/api` service
when it needs platform capabilities. Product repositories consume shared
packages through published versions or an approved workspace integration.

Do not place Kubernetes manifests, secrets, or deployment configuration inside
frontend source code. Those belong under `infra/`.