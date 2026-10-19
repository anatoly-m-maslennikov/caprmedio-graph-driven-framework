---
subjects:
  governs: "Subject Expression Evaluation"
  depends_on:
    ["General Term", "Governed Term", "Subject Expression", "Dependent Entity", "Property", "IS_BORNE_BY", "IS_ALLOWED_VALUE_OF", "Entity/Node/Continuant/Term", "CCE Operator", "Entity/Node/Continuant/Scope Unit.Name", "Subject", "Subject Path"]
version: 19
updated_at: "2026-10-19 15:54:57 +0400"
relations:
  evaluation_for:
    - CA-R-1194
    - CA-R-1931
    - CA-R-1245
    - CA-R-1436
    - CA-M-229
    - CA-R-1324
    - CA-R-1325
    - CA-R-1321
    - CA-R-1275
    - CA-R-1297
atom_id: "CA-E-383"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
---
# Summary

Reject Invalid Subject Expressions

## Scope

Subject Expressions evaluated for invalid component handling.

## Claim

the Evaluation **must** reject a Subject Expression **if**

- `/` does **not** express the approved broader-to-narrower Subject Path profile,
- `.` does **not** encode **`=1`** valid bearer edge from the following Dependent Entity occurrence **to** the immediately preceding bearer occurrence,
- `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436-CORE_META_MODEL-CORE-REQUIREMENT--define-is-allowed-value-of,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Dependent Entity occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- an ordinary named component fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression, **or** an `atom(...)` component is **not** one of that Requirement's registered exact initial selector forms,
- an ordinary General Term is substituted for a required Term reference,
- a Term name **contains** `/`, `.`, **or** `:`,
- `@` is used as a Subject token,
- a complete composite Subject Expression is classified as one Term,
- **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.

## Details

### Term-component cases

`Artifact/Atom.Status: Active` **must** pass the component check **only when** its four named Terms **and** exact qualified target are admitted. `/`, `.`, **and** `:` contribute no Term nodes. `atom(content_role="Plan").Status`, `atom(content_role="Plan",type="Plan").Status`, **and** `atom(atom_id="CA-O-135").Status` **must** pass only in the approved profile when their selector syntax is exact; lowercase `atom` is **not** a Term, **and** its syntax validation neither enumerates a concrete Atom row nor admits a target Entity. `atom(type="Plan").Status`, a mixed `atom_id`/`content_role` selector, a selector after a Subject separator, **and** every selector in legacy **must** fail. an unresolved ordinary named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Entity.

`Atom/Content Role: Requirement/Type: Demand` is retained only as a legacy five-component fixture; it does **not** define an approved all-dot role conjunction or selector grammar.
