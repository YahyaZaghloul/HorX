# Backend

Planned Python application backend. Scanner engines live separately in [scanners/](../scanners/README.md).
This folder contains ownership guides, not a running service.

- `core/`: API, storage, access control and orchestration — Youssef Ashraf and Ahmed Amr.
- `reporting/`: report generation and authorized export — Youssef Ashraf and Ahmed Amr.

**Application-backend owners: Youssef Ashraf and Ahmed Amr, jointly.**
Scanner owners implement engines outside this folder, not separate application backends.

Agree on [shared contracts](../docs/integration.md) before implementing adapters.
Scanner modules must not invent their own databases, job queues or credential stores.
