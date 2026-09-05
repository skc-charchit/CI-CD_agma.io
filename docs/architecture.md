# AGMA.io Architecture and Development Flow

This document explains what runs, where it lives, how a browser request moves
through the repository, and how to validate a change before review.

## 1. Repository responsibilities

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

## 2. What runs locally

The local workflow starts two independent processes:

```text
Browser
  |
  | http://127.0.0.1:5500
  v
python3 -m http.server
  |
  | serves apps/company-web/public/index.html
  v
Company homepage
  |
  | GET http://127.0.0.1:8000/api/v1/courses
  v
uvicorn app.main:app
  |
  v
apps/api/app/api/v1/courses.py
```

The two-process setup is intentional:

- The company website is static browser code and is served on port `5500`.
- The platform API is a FastAPI application and is served on port `8000`.
- The browser calls the API for course data.
- Local CORS settings allow the website origin to call the API.
- In a deployed setup, the frontend uses the relative `/api/v1/courses` path
  behind the same public host.

## 3. Homepage request flow

When a user opens the company website:

1. The browser requests `apps/company-web/public/index.html` through the local
	static server.
2. The browser loads Tailwind CSS, Font Awesome, Google Fonts, and the inline
	JavaScript in the page.
3. The `DOMContentLoaded` handler creates the category navigation.
4. The handler requests `/api/v1/courses`.
5. During local development on port `5500`, the request is sent to
	`http://127.0.0.1:8000/api/v1/courses`.
6. FastAPI receives the request in `app/main.py` and includes the versioned
	courses router.
7. `app/api/v1/courses.py` returns the course catalog JSON.
8. The browser turns that JSON into course cards in
	`#bestsellers-section`.
9. If the API fails, the page logs the error and renders an empty fallback
	section instead of breaking the rest of the page.

The current catalog is in-memory demo data. A database or product service can
replace it later without moving browser code into the API.

## 4. Local development, step by step

From the repository root:

```bash
./scripts/dev.sh
```

That script:

1. Finds the repository root.
2. Starts FastAPI with `PYTHONPATH=apps/api` and Uvicorn on port `8000`.
3. Starts Python's static file server for `apps/company-web/public` on port
	`5500`.
4. Prints the URLs.
5. Stops both child processes when you press `Ctrl+C`.

Open these URLs:

```text
Company website: http://127.0.0.1:5500
API documentation: http://127.0.0.1:8000/docs
Course API: http://127.0.0.1:8000/api/v1/courses
```

Do not open the product template as the company website. It is a starter for a
future product repository.

## 5. Review checks, step by step

Before opening a pull request or pushing for review, run:

```bash
./scripts/check.sh
```

That script:

1. Verifies `uv.lock` matches `pyproject.toml`.
2. Compiles the API Python files.
3. Starts temporary API and website servers on ports `8001` and `5501`.
4. Runs `tests/smoke_test.py` against both services.
5. Confirms the API returns successful course data.
6. Confirms the homepage contains the expected title and API path.
7. Checks the Git diff for whitespace errors.
8. Stops the temporary servers before exiting.

The smoke test intentionally uses Python's standard library, so it does not
need an additional test client dependency.

## 6. Where changes belong

| Change | Location |
| --- | --- |
| Company homepage markup | `apps/company-web/public/index.html` |
| Company frontend components and logic | `apps/company-web/src/` |
| Shared API application setup | `apps/api/app/main.py` |
| Shared API endpoint | `apps/api/app/api/v1/` |
| API validation contracts | `apps/api/app/schemas/` |
| Shared server business operations | `apps/api/app/services/` |
| Reusable UI or types | `packages/ui/` or `packages/types/` |
| Deployment configuration | `infra/` |
| New product starter | `templates/product/` |
| Product implementation | Separate product repository |

Stop at the ownership boundary. Do not place product-specific business rules
in the company website or shared platform API.

## 7. Product example

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