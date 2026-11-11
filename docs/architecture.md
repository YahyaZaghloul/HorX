# Architecture

## Status and scope

Repository organization only. HorX is intended as a Web and Active Directory
vulnerability scanner integrating existing tools, not an autonomous exploitation
framework. No detection, service or storage implementation is present.

## Three top-level components

- `scanners/`: tool adapters, checks, collection, parsers and scanner evidence.
- `frontend/`: analyst interface, scan setup, results and report presentation.
- `backend/`: API, access control, scope, credentials, persistence, job dispatch,
  result ingestion, lifecycle and authorized reporting.

The separation is a code/ownership boundary, not a requirement to create a separate
HTTP service for every engine. Scanner execution stays outside API request handlers.

## Proposed flow

```text
frontend/ (React)
    ↕ documented API
backend/ (FastAPI, storage, orchestration, reporting)
    ↕ versioned execution/result contract through workers/queue
scanners/ (Web and AD engines)
    → observations + evidence references + explicit coverage
backend/ → authorized findings, coverage and reports → frontend/
```

Python/FastAPI, React/TypeScript, PostgreSQL and Redis/Celery are proposed choices.
Workers run tools separately from API requests. A Windows worker is optional only
if an approved AD integration needs it. Review compatibility, licenses and exact
versions before introducing dependencies. No deployment stack is supplied yet.

## Boundaries

- Youssef Ashraf and Ahmed Amr jointly own the application frontend/backend.
- Core owns access control, target scope, credentials, persistence and scan lifecycle.
- Yahya and Ahmed share Web adapters (ZAP/active and baseline/Nuclei respectively);
  Yahya and NourEldin share AD adapters. Scanner modules produce observations, evidence
  references and per-check coverage rather than implementing application services.
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
