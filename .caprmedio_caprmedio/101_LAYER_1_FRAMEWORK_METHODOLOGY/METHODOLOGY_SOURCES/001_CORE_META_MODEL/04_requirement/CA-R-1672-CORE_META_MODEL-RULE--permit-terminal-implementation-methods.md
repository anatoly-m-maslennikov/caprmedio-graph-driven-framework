---
subjects:
  active: Atom
  passive: []
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-030
  - CA-R-1767
atom_id: CA-R-1672
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Permit terminal Implementation Methods

## Claim scope

terminal permission for an active Eng Policy after its local Eng Decisions are absorbed and archived.

## Claim

`eng_policy` **must** be registered as terminal-permitted, so an active Eng Policy Atom **may** remain childless in Atom topology **after** its local Eng Decision Atoms have been losslessly absorbed **and** archived.

## Details

This Atom-topology permission does not create a Scope Unit child or grant local Eng Policy ownership to a leaf; an actual declared child and every-child applicability remain required by CA-R-2119@8.
