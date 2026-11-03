---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Operations)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
version: 24
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-307
  depends_on:
  - CA-M-305
atom_id: CA-M-314
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-314-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-operations-claims-with-type-specific-cce-profiles.md
  source_atom_id: CA-M-314
  source_atom_revision: 24
  source_sha256: 045608078aa047d10884043c9b58d92216978d93a1f2ee053a966d7a6816f9a4
  original_relations_sha256: 3703d8616da3d4b04ccc64fcf5cc23e91071167e8b7cafaa350c16356709907d
---
## Summary

Write Operations Claims with Type-specific CCE Profiles

## Claim scope

Operations Claims written with their admitted Operations Type-specific CCE Profiles.

## Claim

**to** write an Operations Claim, the Author **must** first resolve its admitted Operations Type **and** **then** apply **`=1`** primary Type profile:

1. for Action, use **means** to define the named reusable operational behavior. state its required inputs, preconditions, operational contribution, returned results, observable effects, **and** failure results. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** constrain that behavior.
2. for Workflow, use **means** to define the reusable graph through Step references, entry, typed transitions, result conditions, **and** terminal outcomes. use condition, temporal, logical, restriction, predicate, **and** comparison Operators **only** with explicit transition scope under CA-M-305-CORE_META_MODEL-METHOD--write-workflow-schemes-using-step-references.
3. for Step, define the invocation binding of **`=1`** referenced Action with its parameters **and** inputs. do **not** copy the Action behavior **or** define another Workflow.

## Details

an Operations Claim **must not** combine more than one primary type profile. subordinate inputs, conditions, results, failures, transitions, **and** effects remain part of the selected type's single operational contribution.
