---
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling
version: 31
updated_at: 2026-11-02 18:35:20 +0400
atom_id: CA-R-1627
ref_id: CA-R-1627
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1627-CORE_META_MODEL-RULE--requirement-exclude-secrets-from-caprmedio.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Requirement — Exclude secrets from CAPRMEDIO

## Claim

### Prose Claim


secret values and their use across CAPRMEDIO surfaces.


secret values **must** remain **in** the permitted secret storage defined by CA-D-452. secrets include passwords, API keys, access **or** refresh tokens, session cookies, private keys, signing **or** encryption keys, authentication certificates, one-time **or** recovery codes, **and** connection strings **or** URLs containing credentials.

### authorized use

- Tools **may** receive secrets from that storage, including through host injection, **and** use them for Operator-authorized authentication.
- credential use **must** remain within the authorized transport **and** resource boundary. permission **to** authenticate does **not** authorize disclosure elsewhere.

### excluded surfaces

- secret values **must not** appear **in** Atoms, Project Settings, Framework Instance Settings, generated Artifacts, runtime traces, logs, prompts, checkpoints, Evaluation inputs **and** results, Test fixtures **and** snapshots, evidence, support bundles, issues, pull requests, commits, **or** release records.
- secret values **must** be redacted **before** data enters those surfaces. encoding **or** encrypting a secret does **not** permit its inclusion outside the permitted secret storage.

### personal identifiers

email addresses, usernames, **and** account identifiers are identifiers rather than authenticators. they **may** appear **in** CAPRMEDIO **when** necessary **and** authorized, but **must** be minimized **and** treated as potentially personal data. CAPRMEDIO does **not** become the runtime owner merely because a human-readable Artifact names it.

### exposure response

**if** a secret reaches an unauthorized durable **or** shared surface, stop propagation, revoke **or** rotate it immediately, **then** clean affected Carriers **and** record the incident **without** reproducing the value. deleting a current file is **not** sufficient remediation for a value already present **in** durable history **or** another replica.
