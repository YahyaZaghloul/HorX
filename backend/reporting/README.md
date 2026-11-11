# Reporting

**Owner: Ahmed Amr. Backend reviewer: Youssef Ashraf.**

Implement HTML/PDF/JSON report presentation from authorized normalized data.
Include scan configuration, versions, scope, findings, evidence, remediation,
coverage gaps and retest history. No report exporter exists yet.

The core owns permissions, data access and resolution decisions. Reports must not
recompute lifecycle from missing observations. Escape target-controlled text,
redact secrets, and exclude restricted raw evidence by default.

First deliverable: a report view of the first real integrated scan with visible
failed/skipped checks. Synthetic report fixtures must be labeled as synthetic.
Tests: `tests/reporting/`; suggested branch: `feat/report-templates`.
