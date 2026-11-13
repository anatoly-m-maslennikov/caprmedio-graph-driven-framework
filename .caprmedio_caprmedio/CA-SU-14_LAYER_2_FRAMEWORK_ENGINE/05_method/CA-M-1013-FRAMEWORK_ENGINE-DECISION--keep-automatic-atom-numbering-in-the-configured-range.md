---
identity:
  atom_id: CA-M-1013
  ref_id: CA-M-1013
context:
  role: method
  form: decision
  tier: 3
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:56:10.799172+00:00'
destination:
  file:
    name: CA-M-1013-FRAMEWORK_ENGINE-DECISION--keep-automatic-atom-numbering-in-the-configured-range.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method
---
## Summary

Keep automatic Atom numbering in the configured range

## Claim

### Prose Claim

When Project Settings provides `artifacts.identity.automatic_number_ceiling`, allocate the next number for the Role within `1` through that ceiling. Use the highest in-range number reserved by a Current, Draft or Archived carrier, including Archives whose bodies are not loaded. Treat leading zeros numerically for allocation and preserve their exact spelling in references. Existing IDs above the ceiling remain valid and addressable. Reject a new allocation if the configured range is exhausted. Without a ceiling, retain the unbounded per-Role sequence. CAPRMEDIO sets the ceiling to 999999 so retained throughput probes and the IDs that followed them do not advance ordinary numbering.
