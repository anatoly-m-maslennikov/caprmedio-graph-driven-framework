---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.ID
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 28
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
atom_id: CA-D-378
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Assigned Atom Identities

## Claim

### Prose Claim


assigned Atom IDs.


**every** assigned Current or Archived Atom ID **must** begin with the registered uppercase Project identity prefix. the canonical Project-owned Atom ID encoding **must** match `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-<GLOBAL_NUMBER_WITHIN_CONTENT_ROLE>`. Every Draft Atom **must** carry a Draft-only `atom_id` marker: `<canonical-ID>@<proposed-version>-draft` for a proposed revision of an existing Atom, or `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>-draft` for a new Atom; `@<proposed-version>-draft` occurs once in the ID and matching Draft filename identity segment. A Draft marker is permitted on a Draft source, not a Current source. The role-only new-Atom marker allocates no canonical number. For Archived predecessors, qualify the Atom-ID filename segment and `atom_id` as `<canonical-ID>@<old-version>` exactly once, preserving its numeric Version and Updated At; do not require an exact-byte archive carrier. the Atom Content Role Identity Letter **must** be **in** (Concern: C, "Analysis & Advisory": A, Plan: P, Requirement: R, Method: M, Evaluation: E, Delivery: D, Operations: O). a `<PROJECT_PREFIX>-P` Identifier **must** identify a Plan Atom, including one labeled Epic, **and** **must not** identify a separate non-Atom collection.
