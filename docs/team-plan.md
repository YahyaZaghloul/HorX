# Team ownership and implementation plan

| Member | Owned paths | Primary work |
| --- | --- | --- |
| Youssef Ashraf | `backend/core/`, `backend/reporting/`, `frontend/` (jointly with Ahmed) | Application frontend/backend: APIs, data, orchestration, security, dashboard and reporting |
| Yahya Mohamed | `scanners/web/` (with Ahmed), `scanners/ad/` (with NourEldin) | Web ZAP/active checks; joint AD collection, rules, protocol checks and tests |
| NourEldin | `scanners/ad/` (shared with Yahya) | Joint AD collection, rules, protocol posture, lab and tests |
| Ahmed Amr | `backend/core/`, `backend/reporting/`, `frontend/` (with Youssef); `scanners/web/` (with Yahya) | Joint application work; Web baseline/configuration/exposure checks and curated Nuclei |

**Youssef Ashraf and Ahmed Amr jointly own the application frontend and backend.**
They agree their internal task split; neither is assigned exclusively to one side.
Scanner engines live in top-level `scanners/`, separate from `frontend/` and
`backend/`. They consume shared application contracts/services rather than building
separate APIs, databases or dashboards.

Yahya and NourEldin jointly own AD; their internal AD task split is agreed together.
Shared interfaces are team decisions; Youssef and Ahmed maintain their implementation.
Each member writes their own tests and documentation; the application pair is not
responsible for writing all scanner tests.
Names are ownership labels, not GitHub handles. CODEOWNERS/reviewer automation is
not configured because the other members' account handles were not provided.

## Milestones

1. Approve check catalogue, architecture, schemas and isolated lab inventory.
2. Complete one real Web and AD check end to end before expanding adapter breadth.
3. Add selected integrations and positive/negative/error fixtures.
4. Deliver normalized findings, evidence and transparent coverage.
5. Deliver report export and reliable fix/retest comparison.
6. Harden boundaries, measure results and document reproducible deployment.

The earlier 16-week schedule was a planning assumption, not a confirmed deadline.
No permanent per-member branches are created: use short-lived task branches.

## Done means

Implementation, positive/negative tests, error/coverage behavior, actual execution
results, documentation and another member's review. Do not advertise planned
vulnerabilities as supported. Reduce coverage breadth before dropping scope safety
or trustworthy evidence.
