# Product Repository Template

Products are maintained in separate repositories. Use `templates/product/` as
the starting point when creating a new product repository:

```text
product-name/
├── frontend/
│   ├── src/
│   └── public/
├── backend/
│   └── app/
├── tests/
├── Dockerfile
└── README.md
```

Each product owns its frontend, backend, tests, and release pipeline. Shared
functionality belongs in packages published by the platform repository.
Kubernetes configuration belongs in
`infra/kubernetes/products/product-name/` in this platform repository.