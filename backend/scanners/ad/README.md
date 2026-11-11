# Active Directory scanning engine

**Owner: NourEldin.**

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

Coordinate domain scope/credentials with Youssef and evidence display with Ahmed.
Optional third-party tools require platform and licensing review before integration.
Suggested branches: `feat/ad-directory-collector`, `feat/ad-account-policy-checks`.
