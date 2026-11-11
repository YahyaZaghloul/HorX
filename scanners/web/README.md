# Web scanning engine

**Owners: Yahya Mohamed and Ahmed Amr.**

This is the top-level `scanners/web/` component, separate from the application
frontend and backend. No scanner is implemented by this scaffold.

## Work split

| Owner | Primary Web work |
| --- | --- |
| Yahya Mohamed | ZAP adapter/parser, bounded discovery, authentication verification, selected reflected-XSS, SQL-injection and path-traversal checks |
| Ahmed Amr | Configuration/exposure checks, headers/cookies, CORS, sensitive files, directory listing, verbose errors and curated Nuclei adapter/parser; selected TLS checks later |
| Both | Shared Web entry point, scan profiles, finding identity, overlap handling and integration tests |

Ahmed also jointly owns the application frontend/backend with Youssef Ashraf.
Keep scanner code separate from application services even when one member works
on both. Begin Ahmed's Web scope with baseline checks and a small template subset.

## Proposed module layout

The files below are planned, not implemented:

```text
scanners/web/
├── adapters/
│   ├── zap.py              # Yahya
│   └── nuclei.py           # Ahmed
├── parsers/
│   ├── zap.py              # Yahya
│   └── nuclei.py           # Ahmed
├── checks/configuration/   # Ahmed, where custom checks are needed
├── authentication.py       # Yahya
├── adapter.py              # Shared entry point
├── profiles.py             # Joint review
└── README.md
```

## First deliverable and boundaries

Execute one bounded real check through the shared application contract, with
vulnerable, clean and failure cases. Add [Web tests](../../tests/web/README.md)
and explicitly labeled [synthetic fixtures](../../tests/fixtures/web/README.md).

The application backend supplies scope/credential/evidence services, persistence,
queueing and lifecycle. Scanners return normalized observations and explicit
coverage; they do not implement separate APIs, databases or dashboards.
Keep active checks opt-in. Never claim authenticated coverage after session loss,
or report a failed/skipped check as clean. Preserve source observations when
overlapping findings are grouped. Planned checks are not supported capabilities.

Agree [shared contracts](../../docs/integration.md) before implementation.
Suggested branches: `feat/zap-adapter`, `feat/web-baseline-nuclei`.
