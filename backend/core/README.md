# Core backend and scan orchestration

**Joint owners: Youssef Ashraf and Ahmed Amr.**

Own project/target/scan APIs, persistence and migrations, authentication and project
permissions, credential references and encryption, scope policy, job dispatch,
timeouts, cancellation, finding ingestion, coverage, and retest lifecycle.

Together own the application backend and coordinate API/frontend integration.
Web (Yahya + Ahmed) and AD (Yahya + NourEldin) supply top-level scanner adapters.
Keep adapter logic separate from the application services owned by Youssef + Ahmed.

Maintain shared schemas after team agreement. Workers execute tools outside API
request handlers. Enforce scope centrally and at worker network boundaries.

First deliverable: a reviewed adapter/result contract and a scan lifecycle that
can accept one real Web check and one real AD check through the same pipeline.
Test failures, cancellation, cross-project denial, secret redaction, and retests
that fail or lose access. Never treat failure as a clean result.

Suggested task branches: `feat/project-target-api`, `feat/scan-orchestration`.
Tests belong in `tests/core/` and cross-component tests in `tests/integration/`.
