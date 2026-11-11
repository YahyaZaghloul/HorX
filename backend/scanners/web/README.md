# Web scanning engine

**Owner: Yahya Mohamed.**

Integrate ZAP and a curated, pinned Nuclei template set; implement bounded crawling,
authentication verification, baseline/opt-in active profiles, result parsers,
evidence extraction and explicit coverage. Tool installation is not part of this scaffold.

Planned checks: headers/cookies, diagnostic leakage, sensitive-file exposure,
directory listing, TLS/certificates, CORS, and selected reflected-XSS, SQL-injection,
path-traversal and known-vulnerability rules. None are supported yet.

First deliverable: one bounded real Web check parsed into the shared contract,
with vulnerable, clean and failure cases. Use `tests/web/`; place synthetic,
explicitly labeled samples in `tests/fixtures/web/`.

Coordinate scope and credential handling with Youssef, response/evidence display
with Ahmed. Never claim authenticated coverage after session loss.
Suggested branches: `feat/zap-adapter`, `feat/nuclei-adapter`.
