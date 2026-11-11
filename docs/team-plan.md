# Team ownership and implementation plan

| Member | Owned paths | Primary work |
| --- | --- | --- |
| Youssef Ashraf | `backend/core/` | API, database, queue, scope, credentials, shared contracts, lifecycle |
| Yahya Mohamed | `backend/scanners/web/` | Web integrations, authentication, parsers, Web lab and accuracy |
| NourEldin | `backend/scanners/ad/` | Read-only collection, AD rules, protocol posture, AD lab |
| Ahmed Amr | `frontend/`, `backend/reporting/` | Dashboard, evidence/coverage views, reports and comparison |

Youssef reviews backend reporting integration. Shared interfaces are team decisions.
Each member writes their own tests and documentation; Ahmed is not the team's sole tester.
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
