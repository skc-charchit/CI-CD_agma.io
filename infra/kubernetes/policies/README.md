# Policies

## Owns

Network policies and cluster policy resources that protect workloads and
define permitted communication.

## Put here

Default-deny rules, explicit service-to-service access, pod security settings,
and policy resources shared across applications.

## Do not put here

Application business rules, ingress routing, or secrets.

## Stop here

Default to denying unnecessary traffic and explicitly allow only required
communication. Keep app-specific behavior with the app deployment.