---
artifact_type: question
artifact_subtype: conflict
artifact_id: CAPRMADIO-CONFLICT-GOV-001
scope_path: layer:gov
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relation_kind: conflict_between
endpoints:
  - role: party
    target: CAPRMADIO-DECISION-GOV-003
    origin: internal
  - role: party
    target: CAPRMADIO-REQUIREMENT-GOV-037
    origin: internal
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-DECISION-GOV-003
      - CAPRMADIO-REQUIREMENT-GOV-037
---

# Conflict — All-TOML carriers versus byte-stable YAML history

`CAPRMADIO-REQUIREMENT-GOV-037` requires CAPRMADIO-owned structured artifacts and new
Markdown frontmatter to use TOML, while `CAPRMADIO-DECISION-GOV-003` and its
format-specific descendants require emitted atoms and historical YAML carriers
to remain byte-for-byte unchanged.

The operator now requires the existing ten historical YAML files and all
historical YAML-frontmatter Markdown artifacts to migrate to TOML. The conflict
therefore concerns carrier representation, not the stable semantic identity,
claim, provenance, body, lifecycle, or authority of any artifact.

Resolution requires a Decision that defines whether carrier bytes are part of
atomic identity, names the historical TOML target convention, and requires a
lossless, transactional old-digest to new-digest transition record.

## Primary claim

The requirement that every CAPRMADIO-owned artifact carrier use TOML is incompatible with the active rule that historical and atomic carriers remain byte-stable YAML.

## Rationale

Both directives apply now to the same repository and carrier set, so implementation cannot satisfy both without an explicit authority change.
