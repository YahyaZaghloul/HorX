# Scanner engines

Web and AD adapters share the core's input/output contracts. They collect and
interpret evidence; the core owns persistence, credentials, scheduling and lifecycle.

Declare check identifiers, tool/rule versions, prerequisites, impact, timeouts,
and cancellation behavior. Return observations, evidence references and explicit
per-check outcomes. Read [integration requirements](../../docs/integration.md).

Only scan allowlisted, authorized assets. No unrestricted command/template upload.
