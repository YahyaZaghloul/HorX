# Dashboard and analyst workflow

**Joint owners: Youssef Ashraf and Ahmed Amr.**

Planned stack: React and TypeScript. No application or package manifest is scaffolded yet.

Own project/target setup, credential-entry UI using the core API, scan profiles,
progress/cancellation/errors, findings filters, evidence viewer, coverage,
report presentation and before/after comparison.

Coordinate the internal frontend/backend work split together. Agree API schemas
within the application team and evidence requirements with the Web team
(Yahya + Ahmed) and the AD team (Yahya + NourEldin). Never keep secrets in browser local storage or
render raw scanner HTML.

First deliverable: the first real Web and AD scan shown through the agreed API,
including loading, empty, failed, skipped and inconclusive states. Mock data is
allowed only in clearly labeled development fixtures, not as scan evidence.

Frontend tests should live beside implemented components; cross-system workflow
tests belong in `tests/integration/`. Suggested branch: `feat/scan-setup-ui`.
