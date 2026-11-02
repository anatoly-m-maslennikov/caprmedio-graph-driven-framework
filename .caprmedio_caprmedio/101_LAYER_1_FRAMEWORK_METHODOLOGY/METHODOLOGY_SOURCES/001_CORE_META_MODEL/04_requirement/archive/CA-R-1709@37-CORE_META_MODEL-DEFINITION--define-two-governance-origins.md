---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Governance Origin
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 37
updated_at: 2026-10-29 17:09:47 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1709@37
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define two Governance origins

## Claim scope

Governance Origins of governed Artifacts.

## Claim

Governance Origin is one effective classification under the Project boundary. This logical count does not require another stored copy where Delivery authority derives it from that boundary.

Governance Origin classifies **where** a governed Artifact's primary meaning is owned. Governance Origin has **`=2`** values:

- `internal` **means** the current project establishes **and** owns the meaning;
- `external` **means** an identified source outside the current project establishes **or** imposes the meaning, while the project records **and** binds itself **to** that source.

Governance Origin is independent of Artifact form, Content Role, structural scope, provenance, **and** graph relations. a typed graph relation does **not** create another Governance Origin; its Carrier encoding is governed by CA-D-268.

the current project boundary is ambient. Requirement authority defines these two values **and** the admitted Types; Delivery authority governs their Carrier encoding.

### Formal claim

```text
Entity/Object/Continuant/Governing Objects/Atom.Governance Origin[string]{1}
Entity/Object/Continuant/Governing Objects/Atom.Governance Origin: internal
Entity/Object/Continuant/Governing Objects/Atom.Governance Origin: external
```
