---
atom_id: CA-E-521
ref_id: CA-E-521
container:
  scope_unit: CA-SU-13
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Updated At
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Version
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Atom.Header.Identity.ID
  - CAPRMEDIO_MODEL <+ Entity
tier: 4
relations:
  evaluation_for:
  - CA-D-270
  - CA-R-1432
  - CA-R-1788
  - CA-O-051
status: Active
version: 22
updated_at: 2026-11-02 00:18:22 +0400
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Verify Atom lifecycle Version and Updated At

## Claim

### Prose Claim

This Evaluation checks persisted Atom lifecycle Version and Updated At against CA-R-1432 and CA-R-1788, using source carrier bytes and readback as evidence. Journal recording is independent and is not an acceptance gate for a verified lifecycle effect.

## Details

### Test cases and acceptance criteria

- Edit a Draft, Current and Archived Atom directly in place. Read back each carrier and verify the requested properties and preserved omitted properties, unchanged Version and Updated At. Editing a Draft in place likewise preserves both fields.
- Change a Current Status and archive a Current Atom. Read back each carrier; verify its resulting Status and unchanged Version and Updated At, and that unrelated properties are preserved. Verify against its source bytes that the archived predecessor preserves its base Atom ID, Version, Updated At and unrelated content. Allow the requested Status and model-derived placement, destination, version-qualified Ref ID and filename; those do not create a new base Atom ID.
- Create a Draft for a new version of a Current Atom with unchanged Summary and Content Role. Verify the same identity and Version N+1 at Draft creation. Promote it and verify the promoted Atom retains that Draft Version, with no second increment.
- Change the Draft Summary or Content Role relative to its source. Promote it and verify a new identity at Version 1.
- For composed Update, verify the selected Current's Status is captured and retained at promotion, with source archive preceding successor publication. Verify each distinct eligible Current `IS_REPLACEMENT_FOR` target is archived before publication, and already Archived targets are not archived again.
- Compare persisted source bytes and readback to the requested changes; reject mismatched properties, identity, Version, Updated At, Status, or preservation of unrelated data. Record actual partial effects on a failed effect. A missing or failed Journal observation alone does not fail a verified effect.

The checked rules are CA-D-270, CA-R-1432, CA-R-1788 and CA-O-051. This Evaluation does not establish that a runtime execution occurred.
