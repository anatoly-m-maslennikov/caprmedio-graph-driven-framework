---
subjects:
  governs: "Subject Expression Evaluation"
  depends_on:
    ["General Term", "Governed Term", "Subject Expression", "Subject Target", "Dependent Entity", "Property", "IS_BORNE_BY", "IS_ALLOWED_VALUE_OF", "Entity/Node/Continuant/Term", "CCE Operator", "Entity/Node/Continuant/Scope Unit.Name", "Subject", "Subject Path"]
version: 21
updated_at: "2026-10-21 01:47:52 +0400"
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
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-383-CORE_META_MODEL-EVALUATION_APPROACH--reject-invalid-subject-expressions.md
  source_atom_id: CA-E-383
  source_atom_revision: 21
  source_sha256: ee5854c6af9db01b90f5588813590f30be39047b6cbb33215af177a8b5db21a3
  original_relations_sha256: 5dcebe2528d98c527a3c9c7a2a2d6a914f6023c06cffde0da4b4eccb8a1d8728
---
# Summary

Reject Invalid Subject Expressions

## Scope

Subject Expressions evaluated for invalid component handling.

## Claim

the Evaluation **must** reject a Subject Expression **if**

- `/` does **not** express the approved broader-to-narrower Subject Path profile,
- `//` does **not** occur exactly between an Entity kind component and a following named instance component, or the entire path fails to resolve to exactly one existing canonical Subject Target under CA-R-1202,
- `.` does **not** encode **`=1`** valid bearer edge from the following Dependent Entity occurrence **to** the immediately preceding bearer occurrence,
- `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436-CORE_META_MODEL-CORE--define-is-allowed-value-of,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Dependent Entity occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- an ordinary named component other than the RHS instance name following `//` fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL-CORE--define-subject-expression, **or** an `atom(...)` component is **not** one of that Requirement's registered exact initial selector forms,
- an ordinary General Term is substituted for a required Term reference,
- a Term name **contains** `/`, `.`, **or** `:`,
- `@` is used as a Subject token,
- a complete composite Subject Expression is classified as one Term,
- **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.

For example, in `<kind>//<existing-instance-name>`, the RHS identifies the existing instance and is not automatically a Term; require the complete path to resolve to exactly one existing canonical target. Recognizing `//` alone does not establish or admit an INSTANCE_OF graph fact. Do not reject or accept the name by an Atom-ID pattern; its source/name authority and exact-target resolution govern.

## Details

### Term-component cases

`Artifact/Atom.Status: Active` **must** pass the component check **only when** its four named Terms **and** exact qualified target are admitted. `/`, `.`, **and** `:` contribute no Term nodes. `atom(content_role="Plan").Status`, `atom(content_role="Plan",type="Plan").Status`, **and** `atom(atom_id="CA-O-135").Status` **must** pass only in the approved profile when their selector syntax is exact; lowercase `atom` is **not** a Term, **and** its syntax validation neither enumerates a concrete Atom row nor admits a target Entity. `atom(type="Plan").Status`, a mixed `atom_id`/`content_role` selector, a selector after a Subject separator, **and** every selector in legacy **must** fail. an unresolved ordinary named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Subject Target.

`Method/Decomposition` **must** pass only when `Method` and `Decomposition` are admitted Term references and the complete path resolves to an accepted canonical Method Topic. it must not be classified as an Entity Object or accepted only because a Scope Unit or folder has the same name.

`Atom/Content Role: Requirement/Type: Demand` is retained only as a legacy five-component fixture; it does **not** define an approved all-dot role conjunction or selector grammar.
