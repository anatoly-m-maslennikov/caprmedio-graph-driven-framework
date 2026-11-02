---
subjects:
  governs: Entity
  depends_on:
  - Entity/Object/Continuant/Term
  - Entity
  - Entity/Object/Continuant/Term//Dependent Entity
  - Entity/Object/Continuant/Term//Property
  - Entity/Graph Syntax > Relation//IS_BORNE_BY
  - Entity/Graph Syntax > Relation//IS_ALLOWED_VALUE_OF
  - Entity/Aspect/Engineering/Data Handling/Data Validation
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Name
version: 38
updated_at: 2026-10-29 09:31:44 +0400
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
atom_id: CA-E-383@38
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 4
---
## Summary

Reject Invalid Subject Expressions

## Claim scope

Entity Expressions evaluated for invalid component handling.

## Claim

Under A1296, count an omitted property as zero values, a scalar null as one value, and an empty string as one value. Check the parsed value against the declared Format and applicable prose conditions separately. Do not pass a required string merely because a null satisfies the count; do not reject an empty string solely because it is empty unless the applicable rules require substantive/nonempty content.

For the Entity format check under CA-A-1285, check string-valued content and the admitted notation. Do not fail that format check solely because a defining Atom introduces a new governed entity. Target authority and explicit existing-kind reference resolution are separate semantic checks, not consequences of the string Format.

Under CA-A-1283, admit subjects{0} with one governs reference and zero or more dependencies; reject a direct subjects scalar without rejecting its declared children. Require direct prose for claim{1} even when formal_claim{0..1} is present. For property[string]{2}, require two string values under one key; repeated sibling YAML keys do not satisfy cardinality. Do not treat a sequence as one list-formatted value or count child keys as direct parent values.

Accept Package/Project Implementation as the parentless root Package and each Module only when it belongs to exactly one Package; reject the superseded root-under-Implementation and independent-Module cases.

For cardinality under CA-A-1280, accept `{0}`, `{1}`, `{3}`, `{0+}`, `{1+}`, `{2+}`, `{0..1}` and `{2..5}` with their declared counts. Reject negative or fractional bounds, an empty `{}`, a missing range bound such as `{2..}`, repeated plus signs such as `{1++}`, and an inverted range such as `{5..2}`. A Step count of zero fails Workflow >{1+} Step; zero Substeps is admitted by Step >{0+} Substep. A containment count must not be read as inheritance or as changing the exactly-one immediate-whole rule.

the Evaluation **must** reject an Entity Expression **if**

- `/` does **not** express the approved broader-to-narrower Entity Path profile,
- `//` does **not** occur exactly between an Entity kind component and a following named instance component, or the entire path fails to resolve to exactly one existing canonical Entity Target under CA-R-1202,
- `.` does **not** encode **`=1`** valid bearer edge from the following Dependent Entity occurrence **to** the immediately preceding bearer occurrence,
- `:` does **not** express **`=1`** admitted IS_ALLOWED_VALUE_OF qualification under CA-R-1436-CORE_META_MODEL--define-is-allowed-value-of,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Dependent Entity occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- an ordinary named component other than the RHS instance name following `//` fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL--define-subject-expression, **or** an `atom(...)` component is **not** one of that Requirement's registered exact initial selector forms,
- an ordinary General Term is substituted for a required Term reference,
- a name uses an unescaped reserved operator character as literal text, or has an unmatched final backslash,
- a structural containment edge through `>` is used as an inheritance route,
- an unquoted `@` is used outside the admitted existing-kind modifier positions after `/` or `>`, or such a reference fails to resolve to its intended existing canonical kind,
- a complete composite Entity Expression is classified as one Term,
- **or** a registered CCE Operator is redefined as a Governed Term **or** Scope Unit Name.

For example, in `<kind>//<existing-instance-name>`, the RHS identifies the existing instance and is not automatically a Term; require the complete path to resolve to exactly one existing canonical target. Recognizing `//` alone does not establish or admit an INSTANCE_OF graph fact. Do not reject or accept the name by an Atom-ID pattern; its source/name authority and exact-target resolution govern.

## Details

### Term-component cases

`Artifact/Atom.Status: Active` **must** pass the component check **only when** its four named Terms **and** exact qualified target are admitted. `/`, `.`, **and** `:` contribute no Term nodes. `atom(content_role="Plan").Status`, `atom(content_role="Plan",type="Plan").Status`, **and** `atom(atom_id="CA-O-135").Status` **must** pass only in the approved profile when their selector syntax is exact; lowercase `atom` is **not** a Term, **and** its syntax validation neither enumerates a concrete Atom row nor admits a target Entity. `atom(type="Plan").Status`, a mixed `atom_id`/`content_role` selector, a selector after a Entity separator, **and** every selector in legacy **must** fail. an unresolved ordinary named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Entity Target.

`Method/Decomposition` **must** pass only when `Method` and `Decomposition` are admitted Term references and the complete path resolves to an accepted canonical Method Topic. it must not be classified as an Entity Object or accepted only because a Scope Unit or folder has the same name.

`Atom/Content Role: Requirement/Type: Demand` denotes a qualified narrower Atom kind when the complete canonical target is admitted. Its bare Content Role and Type axes do not acquire Atom properties as intermediate path components. It does not define an all-dot role conjunction or create a named instance.

### Membership and inheritance cases

`Entity/Object/Continuant/Actor/Operator` retains source-backed applicable Actor properties. A shortened, deduplicated or filtered view must not manufacture or strengthen a source constraint. These are proposed semantic checks, not evidence that an executable evaluator has been changed. Exact alternate-path identity, literal-name handling and containment constraints await the decisions recorded in CA-A-1236.

### Containment alternatives

In the complete declared containment structure, each branch is an allowed option. `X > Y` requires a contained Y instance to belong to exactly one immediate whole instance of the permitted kind. Alternative container branches are choices, not simultaneous ownership obligations. An independent declaration can permit an uncontained instance; an existing-kind reference does not grant that permission. Part-to-whole cardinality is one; the number of Y parts per X remains separately constrained. CA-A-1253 records this latest cardinality decision. Every Module belongs to exactly one Package; Package/Project Implementation is the parentless root Package, and nested Packages belong to another Package.

In the governing declaration structure, an independent kind declaration outside structural containment permits that kind without that structural parent. An existing-kind reference `@(...)` does not make another independent declaration. Every Module belongs to exactly one Package; Step belongs to Workflow. A standalone source file is a Module of the root Package, not an independently declared Module. A derived display preserves these source meanings even when its selection omits a declaration or reference. This resolves Q02 in CA-A-1236; repeated display labels alone carry no new permission.
Reject an interpretation that requires every alternative container branch simultaneously merely because several branches are declared. This is a proposed semantic evaluation rule; no executable evaluator is changed.

### Existing-target reference marker

Evaluate `/@` and `>@` as their base relation plus an existing-kind reference. Reject an interpretation that creates another target from that reference or changes inheritance merely because `@` is present. Literal operator characters inside names use the separately defined backslash escape rule; an escaped literal @ is not a reference modifier.

### Literal-character escaping

A slash in `CI\/CD` and a period in `Release 0\.4` are literal name characters, not graph edges. A matched `\\` represents one literal backslash. Reject a final unpaired backslash. Do not treat single or double quotes inside the decoded Entity expression as grouping or name-quoting syntax. YAML outer string quoting is checked at the carrier layer, not as an Entity operator. This is a proposed evaluation rule; no executable parser has changed.

### Reference boundary

Require the existing-kind reference form `@(...)` after `/` or `>`, resolving its unique primary-kind name or current canonical path. Reject missing or unmatched unescaped parentheses and unresolved reference targets. A following `.ID` outside the matching close belongs to the referenced kind, not to the reference text. Preserve the operator's endpoint requirements: `/@(...)` references a narrower kind, not its dependent property. These are Draft semantic checks, not implemented parser behavior.

### Canonical path changes

For the Current view, require references to resolve to the one intended current canonical declaration through its unique primary-kind name or its current canonical path. Do not silently accept a retired path as an alias or guess identity from its leaf name. A completed rename or move must leave its in-scope Current ordinary Entity paths and affected full-path references migrated; name-based references change only when the primary-kind name changes; retained history is not reclassified as an alias. These are proposed evaluation rules, not evidence of a completed source migration or parser change.

### Confirmed independent and contained kinds

In the proposed governing structure, reject a Module without exactly one Package and reject an independent Step without a Workflow. A repeated reference to Step does not create an independent Step kind. Distinguish Scope Unit structural parts from organizational membership: its child Scope Units, Atoms and Projections use >. This evaluates the declared semantics, not label presence in a filtered display.

### Unique primary-kind names

Reject multiple distinct primary-kind declarations with the same canonical name across the effective Entity model. Repeated references to one kind are not duplicate declarations; property names and allowed values remain qualified by their bearers and may repeat. Resolve `@(Module)` to its one uniquely named kind. Reject ambiguous names instead of selecting a branch or merging targets. A branch move alone must not invalidate an unchanged unique-name reference. This is a Draft evaluation contract; no parser or project migration has been run.

### General named-relation notation

For a formal Claim or model edge using `Source ((RELATION_TYPE)) Target`, check the matching unescaped delimiters, exact declared Relation Type, endpoint resolution and applicable Entity Definition constraints. Keep the statement distinct from a canonical governing node selector. Unknown type names and unmatched delimiters fail admission rather than becoming new types. An opposite view is valid only through its defined derived inverse name; no backward operator or separately authored inverse fact is introduced. Existing short-operator, reference, escape and identity checks remain applicable. CA-A-1240 records the syntax decision; this Draft does not implement a parser or evaluator.

### Exactly-one containment cases

Reject a contained part instance with no permitted whole or with more than one immediate whole. Accept Package/Project Implementation as the parentless root Package and a nested Package under another Package. Reject a Module without exactly one Package. Do not infer the number of Modules per Package from the one-parent rule. These are evaluation cases for Draft methodology, not runtime tests.
