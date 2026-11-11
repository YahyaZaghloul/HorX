# Tests

Run the current standard-library scaffold suite from the repository root:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

This only verifies directory guides, ownership, local documentation links and
representative ignored secret/runtime paths. It does not test vulnerability detection.

Planned areas: `core/`, `web/`, `ad/`, `reporting/`, `integration/`, and synthetic
`fixtures/web/` / `fixtures/ad/`. Each module owner supplies their own tests.
When introducing nested Python tests, configure discovery (including package markers
where required) so this CI command actually collects them, or update CI explicitly.

Each real check needs vulnerable, clean, malformed/error and incomplete-coverage
cases. Add integration tests for scope, permissions, redaction, cancellation and
failed retests. Real assessment data must never be used as committed fixtures.
