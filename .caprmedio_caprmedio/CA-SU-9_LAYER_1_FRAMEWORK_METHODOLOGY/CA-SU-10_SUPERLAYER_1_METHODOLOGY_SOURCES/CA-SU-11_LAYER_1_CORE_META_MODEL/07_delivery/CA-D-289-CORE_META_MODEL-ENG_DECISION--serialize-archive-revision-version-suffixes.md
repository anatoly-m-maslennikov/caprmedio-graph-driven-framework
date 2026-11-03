---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier.Canonical Address.Segment
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-289
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Archive Revision Version Suffixes

## Claim

### Prose Claim


Archive Carrier basenames for Archived Atom versions.


**every** Archived Atom Carrier basename **must** serialize the archived Atom's canonical ID with exactly one `@<version>` marker, where `<version>` is the unchanged numeric Version Number of that Archived Atom version. The marker **must** occur in the filename's Atom-ID segment under CA-D-283; do **not** append a second `@<version>` to a basename that already carries the marker. Existing legacy archive basenames are not normalized automatically.
