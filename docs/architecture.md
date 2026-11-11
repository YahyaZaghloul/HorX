# Architecture

## Status and scope

Repository organization only. HorX is intended as a Web and Active Directory
vulnerability scanner integrating existing tools, not an autonomous exploitation
framework. No detection, service or storage implementation is present.

## Proposed flow

```text
React dashboard → FastAPI core → queue → Web / AD workers
                       ↕                       ↓
                  PostgreSQL ← normalized results + coverage
                       ↕
                restricted evidence storage → reporting
```

Python/FastAPI, React/TypeScript, PostgreSQL and Redis/Celery are proposed choices.
Workers run tools separately from API requests. A Windows worker is optional only
if an approved AD integration needs it. Review compatibility, licenses and exact
versions before introducing dependencies. No deployment stack is supplied yet.

## Boundaries

- Core owns access control, target scope, credentials, persistence and scan lifecycle.
- Web/AD adapters produce observations, evidence references and per-check coverage.
- Reporting consumes authorized results; it does not decide whether fixes succeeded.
- Frontend consumes documented API responses rather than scanner-native output.
- Everyone owns tests and documentation for their own module.

## Release requirements

Explicit allowlists/exclusions, DNS and redirect revalidation, worker network
restrictions, structured process arguments, bounded output/resources, cancellation,
secret redaction, safe output rendering and version provenance must be tested.

Failed/skipped/inconclusive checks are not clean checks. Failed retests never resolve
findings. Keep severity, confidence and finding lifecycle separate.

Exclude password spraying, credential dumping, lateral movement, persistence,
automatic remediation and unrestricted exploit execution from the initial release.
Coverage becomes supported only after vulnerable and clean lab cases are validated.
