---
atom_id: CA-R-1844
ref_id: CA-R-1844
container:
  scope_unit: CA-SU-24
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Authoring <+ Prompt Authoring
  dependencies:
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Effect Authorization
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Requirement)
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Delivery)
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Method)
  - MODEL//CAPRMEDIO <+ Atom/(.Header.Context.Role := Evaluation)
tier: 3
status: Active
version: 12
updated_at: 2026-11-10 20:47:54 +0400
carrier_destination:
  file:
    name: CA-R-1844-PROMPTS-RULE--separate-implementation-prompt-input-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/04_requirement
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
## Summary

Separate implementation prompt input authority

## Claim scope

the admitted input packet passed to one current Implementation Workflow prompt.

## Claim

### Prose Claim

the Implementation **must** carry selected active R/D targets as what to implement, one verified complete active-M projection as how to implement, and applicable E atoms as separate checks, each with identity, revision, path, digest, and full required content.

## Details

The M projection is a derived Run input, sorted repeatably and retained downstream; membership does not establish applicability. Missing, stale, conflicting, unauthorized, or incomplete inputs return the source Step's blocked result.
