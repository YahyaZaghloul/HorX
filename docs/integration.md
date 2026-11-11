# Integration agreements

**Design checklist, not an implemented API or finalized schema.** Youssef Ashraf and
Ahmed Amr jointly maintain shared application contracts after all four members
review them. Add versioned concrete schemas and contract tests in the first
implementation PR; do not independently invent formats.

## Component boundary

`frontend/` talks to the authorized `backend/` API. The backend dispatches work to
workers that invoke engines in top-level `scanners/`. Engines return typed results
through agreed contracts; they do not write database rows or expose browser APIs.
Scope enforcement, evidence access, credentials and cancellation must still work
across this boundary. Moving folders alone does not implement that integration.

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

- Youssef + Ahmed → scanner owners: versioned adapter/result schemas, scope and
  credential services, progress/cancellation hooks, evidence services and error shapes.
- Yahya + Ahmed (Web) → application pair: real normalized Web observations and
  coverage, plus parser tests. Ahmed keeps his Web and application responsibilities
  separated by the component contracts.
- Yahya + NourEldin (AD) → application pair: real normalized AD observations and
  coverage, plus parser tests.
- Youssef + Ahmed → UI/reporting: authorized scan/progress/findings/evidence/report
  interfaces; the pair coordinates API consumption and display together.
- All → application pair: evidence requirements, limitations and integration feedback.

Scanner owners do not build separate APIs, databases, credential stores or dashboards.
Application owners do not replace scanner-owner detection/interpretation tests.

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
