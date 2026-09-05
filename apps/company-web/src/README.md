# Website Source

## Owns

This directory owns the company website's pages, components, state, API client
code, search behavior, and product-catalog presentation.

## Put here

Use subdirectories such as `pages/`, `components/`, `api/`, and `data/` as the
frontend grows. Product cards may link to external product applications.

## Do not put here

Server routes, database access, secrets, Kubernetes manifests, or product
business logic. Use `apps/api` or the product repository instead.

## Stop here

Stop at browser behavior. A frontend feature that needs shared server behavior
must define an API contract and continue in `apps/api`.