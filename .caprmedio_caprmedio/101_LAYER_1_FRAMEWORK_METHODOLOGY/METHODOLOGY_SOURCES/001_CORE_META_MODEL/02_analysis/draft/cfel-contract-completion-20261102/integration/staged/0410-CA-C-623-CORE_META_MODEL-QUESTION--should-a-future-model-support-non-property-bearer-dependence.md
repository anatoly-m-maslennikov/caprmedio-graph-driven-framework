---
atom_id: CA-C-623
role: Concern
form: Question
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
priority: medium
subjects:
  active: CFEL <+ Relation//IS_PROPERTY_OF
  passive:
  - CFEL <+ Relation//HAS_PROPERTY
relations: {}
---

## Summary

Should a future model support non-Property bearer dependence?

## Concern

Should a future model support an Entity whose identity depends on an immediate bearer but which is not a Property?

- If yes, define that future Entity and its bearer contract explicitly without treating it as a Property or restoring a superseded Relation merely by name.
- If no, continue to use the Property bearer and inverse contracts for the selected model.

The selected model currently treats a dependent Entity as a Property. The working choice is to adopt IS_PROPERTY_OF and HAS_PROPERTY, then retire the superseded IS_BORNE_BY and BEARS definitions and their inverse Rule. This future-extension question does not block that ordered change.

## Evidences

CA-R-1260 describes a Dependent Entity whose identity requires an immediate bearer. CA-R-1243 defines BEARS as the derived inverse. CA-R-1456 calls those names historical and superseded. The newer IS_PROPERTY_OF and HAS_PROPERTY Declarations describe Property bearing; the Node Declaration classifies Node dependents as Properties. The declared-entity universe also includes entities outside the Node branch, so that Node rule alone does not resolve the wider historical domain.

## Blast radius

A future non-Property dependent Entity would need an explicit bearer contract before it can be admitted. The selected Property contract and the historical predecessor sources remain available without adding an unsupported Relation to the current model.
