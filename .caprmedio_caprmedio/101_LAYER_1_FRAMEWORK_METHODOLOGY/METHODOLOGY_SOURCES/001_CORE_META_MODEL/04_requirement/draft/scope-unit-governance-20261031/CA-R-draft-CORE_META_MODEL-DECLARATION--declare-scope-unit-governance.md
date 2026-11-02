---
atom_id: CA-R-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 3
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
version: 1
updated_at: 2026-10-31 18:43:05 +0400
relations: {}
form: Declaration
---
## Summary

Declare Scope Unit governance

## Claim

A declared Scope Unit has one external Declaration concerning that Scope Unit. The external Declaration is separate from the Scope Unit's internal Tier 0 Contract Atoms.

A Scope Unit Declaration Atom has Role = Requirement and Form = Scope Unit Declaration. Its active Subject (`subjects.active`) identifies the specific Scope Unit instance being declared, not merely the generic Scope Unit kind. Count exactly one matching Declaration Atom per declared Scope Unit. Use this Subject binding; do not require a duplicate binding in Claim or Target Scope Unit. “Active” here names the Subject field, not an added Atom.Status predicate.

The external Declaration may state the Scope Unit's ID, Name, whether it is ordered or unordered, Label, Local Order, and connections. This Draft adds no new format, cardinality or default for those fields. Scope Units do not have Navigation Number. Keep their existing Local Order semantics; do not maintain a duplicate navigation position. Navigation Number is retained only for Steps and P (Plan) Atoms. This decision does not add new numbering or Carrier-format rules for those Atoms.

The Declaration may include optional external Scope Constraints. “External” is relative to the governed Scope Unit; this does not create a new Scope or entity.

The declaration model keeps one or more separate Goal Atoms outside the declared Scope Unit and outside the Declaration. Existing Goal ownership and target conventions remain in force.

Tier 0 Contract Atoms remain internal to the Scope Unit and express its local foundational commitments. A Scope Unit may have zero or more local Contract Atoms. Do not impose a minimum count or require one Contract Atom for every role.

Shared structure belongs in the reusable Declaration model/template. Do not require an additional Definition Atom for each actual Scope Unit.

The model may replace `project_structure.toml` as the governing source after separately authorized adoption; any compatibility TOML would be derived rather than an independently maintained authority. This Draft does not authorize adoption or cutover.

### Formal claim

```
(Atom//.Role = Requirement & .Form = Scope Unit Declaration & .subjects.active = Scope Unit//){:1}
```

This count is applied per specific declared Scope Unit. The expression uses the active Subject field; it introduces no new Role or lifecycle-status predicate. Parser admission is not claimed.

## Details

The Project Declaration is outside the Project, like the Project Goal, following its external Operator ownership. This does not assign a filesystem path or make the Operator a Scope Unit. Scope Units no longer have Navigation Number; Local Order remains.
