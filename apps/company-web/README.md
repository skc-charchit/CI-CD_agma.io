# Company Web

## Owns

This application is the public company homepage, product catalog, search
experience, and company-level navigation.

## Folders

- `public/`: Browser-served entry files and static assets. The canonical
	homepage is `public/index.html`.
- `src/`: Interactive pages, components, API clients, and website-specific
	behavior. Keep new application logic here as the site grows.

The company homepage is `public/index.html`. It consumes the shared course
catalog from `apps/api` at `/api/v1/courses`. Product detail links should open
the owning product application's URL in a new tab.

## Boundaries

The site may display product summaries and link to product detail pages or
product domains. Product business logic, authentication, checkout, and product
backends do not belong here. Shared server-side behavior belongs in `apps/api`.

## Stop here

Stop at the company catalog and navigation boundary. When a feature belongs to
one product, link to that product or implement it in the product repository.