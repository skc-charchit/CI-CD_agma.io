# Product Kubernetes Template

Copy this directory when adding a product. Add shared workload manifests to
`base/`, then create `overlays/dev`, `overlays/staging`, and
`overlays/production` for environment-specific settings.