---
identity:
  atom_id: CA-M-523
  ref_id: CA-M-523@1-draft
context:
  container:
    scope_unit: CA-SU-24
  role: method
  form: solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Authoring <+ Prompt Authoring
    dependencies:
    - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control
      <+ Effect Authorization
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
    - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  tier: 3
state:
  status: draft
  version: 1
  updated_at: 2026-11-10 11:53:32 +0400
destination:
  file:
    name: CA-M-523@1-draft-SOLUTION--separate-implementation-prompt-input-authority.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/05_method/draft
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-1844
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
