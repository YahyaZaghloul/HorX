# Dashboard and analyst workflow

**Owner: Ahmed Amr.**

Planned stack: React and TypeScript. No application or package manifest is scaffolded yet.

Own project/target setup, credential-entry UI using the core API, scan profiles,
progress/cancellation/errors, findings filters, evidence viewer, coverage,
report presentation and before/after comparison.

Coordinate API schemas with Youssef and evidence requirements with Yahya and
NourEldin. Never keep secrets in browser local storage or render raw scanner HTML.

First deliverable: the first real Web and AD scan shown through the agreed API,
including loading, empty, failed, skipped and inconclusive states. Mock data is
allowed only in clearly labeled development fixtures, not as scan evidence.

Frontend tests should live beside implemented components; cross-system workflow
tests belong in `tests/integration/`. Suggested branch: `feat/scan-setup-ui`.
