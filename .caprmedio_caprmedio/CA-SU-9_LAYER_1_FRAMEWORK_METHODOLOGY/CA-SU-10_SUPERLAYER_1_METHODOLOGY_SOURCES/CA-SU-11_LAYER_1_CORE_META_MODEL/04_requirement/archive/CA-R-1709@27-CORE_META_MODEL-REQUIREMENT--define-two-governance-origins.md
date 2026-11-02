---
subjects:
  governs: Governance Origin
  depends_on:
  - semantics
version: 27
updated_at: 2026-10-24 10:48:25 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1709@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define two Governance origins

## Scope

Governance Origins of governed Artifacts.

## Claim

Governance Origin classifies **where** a governed Artifact's primary meaning is owned. Governance Origin has **`=2`** values:

- `internal` **means** the current project establishes **and** owns the meaning;
- `external` **means** an identified source outside the current project establishes **or** imposes the meaning, while the project records **and** binds itself **to** that source.

Governance Origin is independent of Artifact form, Content Role, structural scope, provenance, **and** graph relations. a typed graph relation does **not** create another Governance Origin; its Carrier encoding is governed by CA-D-268.

the current project boundary is ambient. Requirement authority defines these two values **and** the admitted Types; Delivery authority governs their Carrier encoding.

## Details
