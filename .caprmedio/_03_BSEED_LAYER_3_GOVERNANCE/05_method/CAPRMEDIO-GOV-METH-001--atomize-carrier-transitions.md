---
subject_scopes:
  - carrier-format
tier: core
version: 4
updated_at: 2026-08-20 18:32:49
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMEDIO-GOV-METH-028--semantic-immutability-and-toml-carriers
  child_of:
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---

# Atomize carrier transitions

Moving a carrier between directories while preserving its bytes and assigned
`atom_id` is not a semantic transition and needs no location record. The
identity resolver finds the current carrier by reading the `atom_id` property
inside the selected `.caprmedio`; it does not treat the mutable filename as the
identity authority.

A carrier-name or representation migration is one immutable transition record,
not an entry in a shared ledger. It records the `atom_id`, old and new carrier
names, old and new digests, semantic-equivalence proof, Git return identity,
implementation commit, session provenance, and declared loss. It never stores
the old or new physical path as current authority.

A semantic change is not a carrier transition; it requires a successor atom
with a new `atom_id` and the applicable lifecycle relation.
