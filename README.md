# HorX

Web application and Active Directory vulnerability-assessment project.

**Status: repository scaffold only.** No scanner, API, frontend application,
database, workers, or vulnerability detection has been implemented yet.

## Repository layout

```text
HorX/
├── scanners/             # Independent scanner engines
│   ├── web/              # Yahya Mohamed + Ahmed Amr
│   └── ad/               # Yahya Mohamed + NourEldin
├── frontend/             # Youssef Ashraf + Ahmed Amr
├── backend/              # Youssef Ashraf + Ahmed Amr
│   ├── core/             # APIs, data, jobs and shared services
│   └── reporting/        # Authorized report generation
├── tests/                # Each member tests their own module
├── docs/                 # Architecture and integration agreements
├── .github/workflows/    # Repository structure checks
├── .gitignore
└── README.md
```

Folders contain responsibility guides so Git tracks them without empty placeholders.

## Ownership boundaries

- **Youssef Ashraf and Ahmed Amr jointly own the application frontend and backend:**
  APIs, database, authentication/authorization, credentials, orchestration, reporting
  and dashboard integration. They coordinate the internal division of this work.
- **Yahya Mohamed and Ahmed Amr share the Web scanner:** Yahya leads ZAP,
  authenticated discovery and selected active checks; Ahmed leads configuration/
  exposure checks and curated Nuclei integration. Both own their tests/fixtures.
- **Yahya Mohamed and NourEldin share the AD scanner:** collection, rules, protocol
  checks and AD tests/fixtures. They coordinate the internal AD task split.

The three top-level components are `scanners/`, `frontend/` and `backend/`.
Scanner engines are no longer nested inside the application backend. They consume
versioned execution/result contracts and services supplied by Youssef and Ahmed.
Folder separation does not require three separate network services.

## Start here

- [Architecture and module boundaries](docs/architecture.md)
- [Shared integration contracts](docs/integration.md)
- [Team ownership and first milestones](docs/team-plan.md)
- [Contribution and branch workflow](CONTRIBUTING.md)
- [Test organization](tests/README.md)

## Verify the scaffold

From the repository root, with Python 3 installed:

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

This checks the scaffold, not scanner behavior. Application installation and
startup commands will be added with the first runnable vertical slice.

## Intended direction

Proposed stack: Python/FastAPI, React/TypeScript, PostgreSQL, Redis/Celery.
Web integrations: ZAP and curated Nuclei templates. AD: authenticated read-only
collection and selected bounded protocol checks. These are plans, not installed
or supported capabilities. Select and lock dependency versions in implementation PRs.

Use HorX only against explicitly authorized targets. Never commit credentials,
real assessment evidence, domain exports, or sensitive reports.
