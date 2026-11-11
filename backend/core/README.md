# Core backend and scan orchestration

**Owner: Youssef Ashraf.**

Own project/target/scan APIs, persistence and migrations, authentication and project
permissions, credential references and encryption, scope policy, job dispatch,
timeouts, cancellation, finding ingestion, coverage, and retest lifecycle.

Maintain shared schemas after team agreement. Workers execute tools outside API
request handlers. Enforce scope centrally and at worker network boundaries.

First deliverable: a reviewed adapter/result contract and a scan lifecycle that
can accept one real Web check and one real AD check through the same pipeline.
Test failures, cancellation, cross-project denial, secret redaction, and retests
that fail or lose access. Never treat failure as a clean result.

Suggested task branches: `feat/project-target-api`, `feat/scan-orchestration`.
Tests belong in `tests/core/` and cross-component tests in `tests/integration/`.
