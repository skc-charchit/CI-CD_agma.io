# Scripts

## Owns

Repository-wide development, testing, validation, generation, and release
automation.

## Put here

Repeatable non-application commands that coordinate multiple apps or packages.
Scripts should be safe to run from the repository root and document required
environment variables.

Available workflows:

- `./scripts/dev.sh`: runs the company website on port `5500` and API on port
	`8000`.
- `./scripts/check.sh`: runs dependency, Python compilation, smoke, and diff
	checks before review.

## Do not put here

Runtime application code, secrets, generated artifacts, or product-specific
deployment logic.

## Stop here

Keep scripts orchestration-focused. The behavior they invoke belongs in the
owning application or package.