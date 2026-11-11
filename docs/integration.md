# Integration agreements

**Design checklist, not an implemented API or finalized schema.** Youssef maintains
shared contracts after all four members review them. Add versioned concrete schemas
and contract tests in the first implementation PR; do not independently invent formats.

## Adapter input

Agree on project/scan/target identifiers, normalized scope and exclusions, selected
check IDs, credential references (never plaintext in job payloads), request budgets,
deadlines, tool/rule versions, progress events and cancellation semantics.

## Adapter output

Agree on stable check ID, asset and affected location, observation title/category,
severity and rationale, confidence, evidence references, tool/rule versions,
timestamps, errors and coverage. Preserve original observations when grouping duplicates.
Raw evidence is restricted; sanitize excerpts displayed in UI/reports.

Keep these distinct:

| Dimension | Intended values |
| --- | --- |
| Check outcome | finding, no finding, skipped, failed, inconclusive |
| Evidence status | observed configuration, scanner-reported, independently validated |
| Finding lifecycle | new, persistent, resolved, accepted risk, not retested |

A missing observation is not resolution. A relevant successful retest must have
comparable scope/access and appropriate rule coverage before resolving a finding.

## API and ownership handoffs

- Youssef → all: versioned adapter/result schemas, API contract and error shapes.
- Yahya/NourEldin → Youssef: real normalized observations and coverage, plus parser tests.
- Youssef → Ahmed: authorized scan/progress/findings/evidence/report interfaces.
- Ahmed → all: UI/report requirements and integration feedback.

Coordinate schema, dependency, migration and configuration edits before coding.
Document compatibility changes in the same PR as implementation and tests.

## First vertical slice

1. Agree on schemas and safe scope representation.
2. Execute one bounded real Web check and one read-only real AD check in isolated labs.
3. Ingest and persist observations, evidence and per-check outcomes through the core.
4. Show findings and failures in the dashboard and report view.
5. Exercise cancellation, access failures and a fix/retest without false resolution.

Do not replace blocked real execution with fabricated output. Synthetic fixtures
must be explicitly labeled and are for tests only, not evaluation evidence.
