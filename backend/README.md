# Backend

Planned Python backend with a modular core and separately executed scanner workers.
This folder contains ownership guides, not a running service.

- `core/`: API, storage, access control and orchestration — Youssef Ashraf.
- `scanners/web/`: Web integrations — Yahya Mohamed.
- `scanners/ad/`: AD assessment — NourEldin.
- `reporting/`: report generation — Ahmed Amr, with Youssef reviewing backend access.

Agree on [shared contracts](../docs/integration.md) before implementing adapters.
Scanner modules must not invent their own databases, job queues or credential stores.
