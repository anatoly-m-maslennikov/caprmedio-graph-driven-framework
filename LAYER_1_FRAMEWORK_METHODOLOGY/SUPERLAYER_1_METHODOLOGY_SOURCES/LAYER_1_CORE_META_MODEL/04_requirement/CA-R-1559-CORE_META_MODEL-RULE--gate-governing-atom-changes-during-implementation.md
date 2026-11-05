---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/AI Agent
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Autonomous Confidence Threshold'
  - CAPRMEDIO_MODEL <+ Atom
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Project
  - 'CAPRMEDIO_STRUCTURE <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)//Implementation Workflow'
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-261
atom_id: CA-R-1559
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Gate governing Atom changes during implementation

## Claim

### Prose Claim


changes to governing RMED Atoms during implementation.


authorization **to** change a governing RMED Atom during implementation **must** satisfy the following Actor policy:

- resolve the Atom's effective Author **before** the proposed change, its governing permissions, the effective Plan Autonomous Confidence Threshold under CA-R-1591, **and** **all** additional Operator rules.
- obtain Operator approval **before** changing an Operator-authored Atom.
- request Operator disposition **before** changing an AI-authored Atom **when** confidence is below the threshold **or** an additional rule requires approval.
- an AI-authored Atom **may** change autonomously **only** **when** confidence is at **or** above the threshold **and** **all** applicable permissions **and** Operator rules allow it.
- a prohibition remains a prohibition; authorship **or** confidence **must not** create permission.
- a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080@29.
- an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.
