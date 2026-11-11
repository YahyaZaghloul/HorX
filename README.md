# HorX

Web application and Active Directory vulnerability-assessment project.

**Status: repository scaffold only.** No scanner, API, frontend application,
database, workers, or vulnerability detection has been implemented yet.

## Repository layout

```text
HorX/
├── backend/
│   ├── core/             # Youssef Ashraf
│   ├── scanners/
│   │   ├── web/          # Yahya Mohamed
│   │   └── ad/           # NourEldin
│   └── reporting/        # Ahmed Amr; backend review by Youssef
├── frontend/             # Ahmed Amr
├── tests/                # Each member tests their own module
├── docs/                 # Architecture and integration agreements
├── .github/workflows/    # Repository structure checks
├── .gitignore
└── README.md
```

Folders contain responsibility guides so Git tracks them without empty placeholders.

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
