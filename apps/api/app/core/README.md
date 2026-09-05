# API Core

## Owns

Cross-cutting API concerns such as security, middleware, logging, and shared
runtime helpers.

## Do not put here

Endpoint-specific logic, database models, or frontend behavior.

## Stop here

Only add code used across multiple API capabilities. Keep feature behavior in
its route, service, schema, or model boundary.
