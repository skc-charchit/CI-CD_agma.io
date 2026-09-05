# Tests

## Owns

Automated checks that verify application behavior before review or deployment.

## Put here

Unit, integration, and smoke tests that can run from the repository root. Keep
external services mocked or explicitly started by the test workflow.

## Do not put here

Application source code, generated output, secrets, or manual development
scripts.

## Stop here

A test should verify an owning application's contract. Fix the application in
`apps/` or `packages/`; do not hide implementation changes inside a test.
