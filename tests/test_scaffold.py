"""Repository organization checks; no vulnerability detection is exercised."""
from pathlib import Path
import re
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ScaffoldTests(unittest.TestCase):
    def test_required_guides_exist(self):
        paths = (
            "backend/core", "backend/scanners/web", "backend/scanners/ad",
            "backend/reporting", "frontend", "tests", "tests/core", "tests/web",
            "tests/ad", "tests/reporting", "tests/integration",
            "tests/fixtures/web", "tests/fixtures/ad", "docs",
        )
        for path in paths:
            with self.subTest(path=path):
                self.assertTrue((ROOT / path / "README.md").is_file())
        self.assertTrue((ROOT / ".github/workflows/ci.yml").is_file())

    def test_owners_documented(self):
        for path, owner in (
            ("backend/core", "Youssef Ashraf"),
            ("backend/scanners/web", "Yahya Mohamed"),
            ("backend/scanners/ad", "NourEldin"),
            ("backend/reporting", "Ahmed Amr"),
            ("frontend", "Ahmed Amr"),
        ):
            with self.subTest(path=path):
                self.assertIn(owner, (ROOT / path / "README.md").read_text())

    def test_local_markdown_links_resolve(self):
        for document in ROOT.rglob("*.md"):
            if ".git" in document.relative_to(ROOT).parts:
                continue
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", document.read_text()):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(document=str(document), target=target):
                    self.assertTrue((document.parent / target.split("#", 1)[0]).exists())

    def test_sensitive_and_runtime_paths_ignored(self):
        for path in (".env", ".env.local", "credentials/test.json", "secrets/key.txt",
                     "evidence/raw.json", "reports/private.pdf", "frontend/node_modules/a.js",
                     "backend/__pycache__/a.pyc"):
            result = subprocess.run(
                ["git", "check-ignore", "--no-index", "-q", path], cwd=ROOT,
                check=False,
            )
            with self.subTest(path=path):
                self.assertEqual(result.returncode, 0)
        result = subprocess.run(
            ["git", "check-ignore", "--no-index", "-q", ".env.example"],
            cwd=ROOT, check=False,
        )
        self.assertEqual(result.returncode, 1)


if __name__ == "__main__":
    unittest.main()
