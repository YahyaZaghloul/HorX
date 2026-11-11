# Scanner engines

Web and AD adapters share the core's input/output contracts. They collect and
interpret evidence; the core owns persistence, credentials, scheduling and lifecycle.

Youssef Ashraf and Ahmed Amr jointly own that application backend and the frontend.
The Web and AD engines are top-level peers of frontend/ and backend/.
Web owners are Yahya Mohamed (ZAP/active checks) and Ahmed Amr (baseline/Nuclei);
Yahya Mohamed and NourEldin share AD. Ahmed also shares application ownership
with Youssef, but those
services stay in backend/ and frontend/, not inside scanner modules.

Declare check identifiers, tool/rule versions, prerequisites, impact, timeouts,
and cancellation behavior. Return observations, evidence references and explicit
per-check outcomes. Read [integration requirements](../docs/integration.md).

Only scan allowlisted, authorized assets. No unrestricted command/template upload.
