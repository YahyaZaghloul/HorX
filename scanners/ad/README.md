# Active Directory scanning engine

**Owners: Yahya Mohamed and NourEldin.**

Agree the internal AD task split together and review each other's changes.
Both owners contribute tests and documentation; no exclusive per-check split is
assigned by this guide.

Build authenticated read-only directory collection, account/policy/delegation and
membership rules, selected SMB/LDAP posture checks, evidence extraction and
permission-gap reporting. No live collection is implemented in this scaffold.

Planned checks include preauthentication disabled, unconstrained delegation,
password-related flags, policy deviations, privileged membership review and
inactive privileged accounts. Distinguish review items from proven weaknesses.
An SPN does not prove a crackable password; a flag does not prove an empty password.

First deliverable: one real read-only AD check using the shared result contract,
with vulnerable/clean lab cases and missing-permission behavior. Use `tests/ad/`
and synthetic `tests/fixtures/ad/`. Keep real directory exports out of Git.

Your responsibility is the AD engine, its tests and documentation—not the
application frontend or shared backend. Youssef Ashraf and Ahmed Amr jointly
provide those services; coordinate domain scope, credentials and evidence with both.
Optional third-party tools require platform and licensing review before integration.
Suggested branches: `feat/ad-directory-collector`, `feat/ad-account-policy-checks`.
