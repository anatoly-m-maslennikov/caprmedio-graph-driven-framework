---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom.Header.Status: Active'
  - CAPRMEDIO_MODEL <+ Entity//Object//Continuant//Actor//Operator
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO_MODEL <+ CFEL
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Data Validation
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Scope Unit.Name
version: 47
updated_at: 2026-11-05 16:33:24 +0400
relations:
  evaluation_for:
  - CA-R-1194
  - CA-R-1931
  - CA-R-1245
  - CA-M-229
  - CA-R-1324
  - CA-R-1325
  - CA-R-1321
  - CA-R-1275
  - CA-R-1297
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-E-383
status: Draft
tier: 4
role: Evaluation
form: Eval Policy
carrier_destination:
  file:
    name: CA-E-383@47-draft-CORE_META_MODEL-EVAL_POLICY--reject-invalid-subject-expressions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
---
## Summary

Reject Invalid Subject Expressions

## Claim

### Prose Claim


Entity Expressions evaluated for invalid component handling.


Under A1296, count an omitted property as zero values, a scalar null as one value, and an empty string as one value. Check the parsed value against the declared Format and applicable prose conditions separately. Do not pass a required string merely because a null satisfies the count; do not reject an empty string solely because it is empty unless the applicable rules require substantive/nonempty content.

For the Entity format check under CA-A-1285, check string-valued content and the admitted notation. Do not fail that format check solely because a defining Atom introduces a new governed entity. Target authority and explicit existing-kind reference resolution are separate semantic checks, not consequences of the string Format.

Under CA-A-1283, admit subjects{0} with one governs reference and zero or more dependencies; reject a direct subjects scalar without rejecting its declared children. Require no direct Claim value and one or both declared Formal Claim and Prose Claim children. For property[string]{2}, require two string values under one key; repeated sibling YAML keys do not satisfy cardinality. Do not treat a sequence as one list-formatted value or count child keys as direct parent values.

Accept Package/Project Implementation as the parentless root Package and each Module only when it belongs to exactly one Package; reject the superseded root-under-Implementation and independent-Module cases.

For cardinality under CA-A-1280, accept `{::0}`, `{::1}`, `{::3}`, `{::0+}`, `{::1+}`, `{::2+}`, `{::0..1}` and `{::2..5}` with their declared counts. Reject negative or fractional bounds, an empty `{}`, a missing range bound such as `{::2..}`, repeated plus signs such as `{::1++}`, and an inverted range such as `{::5..2}`. `$journal[<Journal>] {::0}((CONTAINS))` and `$journal[<Journal>] {::1+}((CONTAINS))` exercise zero and positive outgoing containment bounds over all admissible Event Record targets; an omitted reverse slot remains unspecified. A containment count is independent of inheritance and constrains an endpoint only when its explicit slots or applicable endpoint specification say so.

the Evaluation **must** reject an Entity Expression **if**

- `/` does **not** express the approved broader-to-narrower Entity Path profile,
- a typed instance selector does **not** identify an existing instance of its declared Kind, or the entire selector fails to resolve to exactly one canonical Entity Target that already exists or is explicitly introduced by applicable defining authority under CA-R-1194 and CA-R-1321,
- `.` does **not** encode **`=1`** valid bearer edge from the following Property occurrence **to** the immediately preceding bearer occurrence,
- `:=` does **not** express an admitted allowed value of its preceding X under CA-R-1245-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon,
- `.Header.Form` is interpreted as a primary Entity **or** as a Property subtype of Atom instead of as a Property relative to Atom,
- `Atom/(.Header.Form: Method)` is used as syntax-only evidence that Method is admitted as a Form,
- superseded bare `X/Y: Z` qualification spelling is used in this proposal,
- `>|` or `|<` is interpreted as membership through IS_CLASSIFIED_BY instead of the HAS_CLASSIFICATION axis,
- `*` ranges beyond admitted Atom Status values in a Status classification,
- `/` is interpreted as anything other than one immediate containment fact, its Whole/Part direction is swapped, **or** it is used as inheritance,
- Current fails to exclude Draft and Archived within the admitted Atom Status values,
- a Relation count is interpreted as only an outgoing count despite its two slots, a post-operator slot is treated as outgoing rather than reverse, **or** equivalent forward and reverse writings are given different constraints,
- allowed-value admission is treated as assignment **to** a particular Property occurrence **or** as determining its cardinality,
- a Property occurrence lacks **`=1`** immediate bearer,
- a reusable Term is rejected **only** for changing ordinal position,
- a Governed Term begins with a lowercase letter,
- an ordinary named component other than the Name condition in a typed instance selector fails **to** resolve **to** a Term under CA-R-1321-CORE_META_MODEL--define-subject-expression,
- an ordinary General Term is substituted for a required Term reference,
- a name uses an unescaped reserved operator character as literal text, or has an unmatched final backslash,
- a structural containment edge through `/` is used as an inheritance route,
- a qualified reference fails to resolve to its intended already declared Entity,
- a complete composite Entity Expression is classified as one Term,
- **or** an admitted CFEL notation literal is redefined as a Governed Term **or** Scope Unit Name.

For example, `$instance[<Kind>, (.Name = Instance Name)]` identifies the named instance and is not automatically a Term; require the complete selector to resolve to exactly one canonical target that already exists or is explicitly introduced by applicable defining authority. References must resolve to their intended declared targets. Recognizing a typed selector alone does not establish or admit an INSTANCE_OF graph fact. Do not reject or accept the name by an Atom-ID pattern; its source/name authority and exact-target resolution govern.

For CFEL Formal Claims, accept full-line `# model` and `# instances` comments in one fence, with MODEL first when both groups occur. Do not interpret the comments, variables or nested Markdown headings as declared Properties. Continue to read historical ungrouped Claims and existing bare population selectors; new authoring uses the applicable explicit binder.

Accept `IF $x in (Node, Node.**) THEN ($x.Name: [string]{:1}; $x.Status: [string]{:1})` as one MODEL binding expression. Its unbound variable ranges over the selection; an already bound variable is tested against that same selection. Statements inside its parenthesized conclusion share the binding. Reject treating the variable as a declared Node, executing nested statements without the binding, or introducing a FOR operator.

Accept a typed participant over the selected Action-or-Workflow logical population. Accept an explicit binder before the unchanged filter in `$event_record[<Event Record>, (.object_output{=1}, .object_output.id = $projection.ID)]`. In `MAX($event_record[<Event Record>, (.object_output{=1}, .object_output.id = $projection.ID)].happened_at)`, retain the filtered population as the aggregate argument; do not force a separate aggregate per bound row.

Accept `$x[<Node>]{::1..3}` as a count of the distinct selected logical instances in context, not a one-row count for `$x`; repeated references or Carrier representations of an instance do not multiply the count. A typed anonymous selector can state the same selected population. A named Relation selector such as `$relation[<Relation>, (.Name = NAME)]` and quoted syntax literals retain their identity and text. MODEL Relation descriptor variables stay MODEL evidence; a binder does not create an entity, a Relation fact, an inverse permission or endpoint cardinality.

These variable forms occur in Formal Claims. They do not relax the separate Subject-expression requirement that a named typed selector resolve to its intended declared target. Validate MODEL Property format and count authority from applicable Requirement / Declaration sources separately from syntax recognition; other RMED Claims do not become MODEL Declaration authority.

## Details

### Term-component cases

`Atom.Header.Status := Active` **must** pass the component check **only when** its named lexical components **and** exact qualified target are admitted. `/`, `.`, **and** `:=` contribute no Term nodes. `Atom/(.Header.Role := Plan)/(.Header.Form := Epic).Header.Status` **must** pass only when its components and qualified target are admitted; its syntax alone does not admit values or a target. An unadmitted Role or Form value **must** fail. an unresolved ordinary named component **must** fail the source-reference check; the diagnostic **must** preserve the unresolved reference **without** supplying an invented definition. a complete composite path **must not** be admitted as **`=1`** Term merely because it resolves **to** **`=1`** Entity Target.

Use an admitted Method Atom whose actual GOVERNS target is `Atom.Content`; retain the fixture's source Atom and exact Revision. Check that complete target against its governing authority separately from component-Term meaning. The Method Content Role does not create a Method Subject root or determine the target's category. A Scope Unit, folder, or Carrier spelling cannot substitute for the target binding.

The schematic expression `Atom/(.Header.Form: Method)` denotes an Atom qualified by its own Form Property value; the result is narrower than Atom and inherits applicable Atom features and constraints. `.Header.Form` is relative to Atom, not a primary Entity or a Property subtype of Atom. `Atom/(.Header.Role: Method)` is the concrete canonical example because Method is already a Role; its notation alone does not admit Method as a Form. Neither form creates an intermediate Entity kind, a named instance, or membership through IS_CLASSIFIED_BY. Reject the superseded bare `X/Y: Z` spelling in this proposal while preserving unchanged Current sources and runtime.

### Relation-cardinality cases

Accept `Workflow {::1+}/{::1} Step` as an explicit constraint: every Workflow has one or more contained Steps and every Step has exactly one immediate Whole. Accept a one-sided slot as specified while its absent counterpart remains unspecified. Accept `Property {::1}((IS_PROPERTY_OF)) Bearer` only as one outgoing IS_PROPERTY_OF link per Property; a postfix-only Relation count constrains the reverse count per Bearer. Reject treating a Relation slot as a direct-value count, relation arity, or a count of endpoint nodes. Direct values remain separately counted by `Property[format]{count}`.

### Classification and containment cases

Accept the following only when `>|` denotes HAS_CLASSIFICATION, `/` denotes immediate containment from Whole to Part, and `*` ranges only over admitted Atom Status values:

Require the retained direct fact Part IS_CONTAINED_BY Whole; CONTAINS is its
derived inverse. `Whole/Part` expresses that fact.

```text
Atom.Header.Status >| Status Group:=Draft/Draft
Atom.Header.Status >| Status Group:=Archived/Archived
Atom.Header.Status >| Status Group:=Current/(* not in (Draft, Archived))
```

Reject reading `>|` or `|<` as membership, swapping containment direction, using containment as inheritance, using `*` for arbitrary values, reversing Current's exclusion of Draft and Archived, treating a relative Property qualification as a primary Entity or Property subtype, or inferring Type admission from `Atom/(.Header.Form: Method)`. These are proposed Draft semantic checks, not evidence that an executable parser or evaluator has changed.

### Membership and inheritance cases

`Entity//Object//Continuant//Actor//Operator` retains source-backed applicable Actor properties. This is model narrowing, not an instance selector. A shortened, deduplicated or filtered view must not manufacture or strengthen a source constraint. These are proposed semantic checks, not evidence that an executable evaluator has been changed. Exact alternate-path identity, literal-name handling and containment constraints await the decisions recorded in CA-A-1236.

### Containment alternatives

In the complete declared containment structure, each branch is an allowed option. `X/Y` permits immediate containment of Y by X; it does not itself require Y to have exactly one Whole. Alternative container branches are choices, not simultaneous ownership obligations. An independent declaration can permit an uncontained instance; a reference does not grant that permission. Any Part-to-Whole or Whole-to-Part cardinality must be stated in explicit endpoint slots or an applicable endpoint specification. CA-A-1253 records the separate Module and Package cardinality decision: every Module belongs to exactly one Package; Package/Project Implementation is the parentless root Package, and nested Packages belong to another Package.

In the governing declaration structure, an independent kind declaration outside structural containment permits that kind without that structural parent. A qualified reference to an already declared Entity does not make another independent declaration. Every Module belongs to exactly one Package; Step belongs to Workflow. A standalone source file is a Module of the root Package, not an independently declared Module. A derived display preserves these source meanings even when its selection omits a declaration or reference. This resolves Q02 in CA-A-1236; repeated display labels alone carry no new permission.
Reject an interpretation that requires every alternative container branch simultaneously merely because several branches are declared. This is a proposed semantic evaluation rule; no executable evaluator is changed.

### Existing-target references

Resolve each qualified reference to its declared target, preserving its canonical identity and defining-source provenance. A reference does not create a duplicate or change containment or inheritance.

### Literal-character escaping

A slash in `CI\/CD` and a period in `Release 0\.4` are literal name characters, not graph edges. A matched `\\` represents one literal backslash. Reject a final unpaired backslash. Do not treat single or double quotes inside the decoded Entity expression as grouping or name-quoting syntax. YAML outer string quoting is checked at the carrier layer, not as an Entity operator. This is a proposed evaluation rule; no executable parser has changed.

### Reference boundary

Require a qualified reference to resolve to its intended declared target. Parentheses group expressions without creating another Entity. Reject unresolved targets and unmatched grouping parentheses. A following `.ID` addresses the referenced Entity’s Property. Preserve the operator’s endpoint requirements: a `//` segment addresses a narrower kind, not its dependent Property. These are semantic checks, not implemented parser behavior.

### Canonical path changes

For the Current view, require references to resolve to the one intended current canonical declaration through its unique primary-kind name or its current canonical path. Do not silently accept a retired path as an alias or guess identity from its leaf name. A completed rename or move must leave its in-scope Current ordinary Entity paths and affected full-path references migrated; name-based references change only when the primary-kind name changes; retained history is not reclassified as an alias. These are proposed evaluation rules, not evidence of a completed source migration or parser change.

### Confirmed independent and contained kinds

In the proposed governing structure, reject a Module without exactly one Package and reject an independent Step without a Workflow when the applicable endpoint specification states that count. A repeated reference to Step does not create an independent Step kind. Distinguish Scope Unit structural parts from organizational membership: its child Scope Units, Atoms and Projections use `/`. This evaluates the declared semantics, not label presence in a filtered display.

### Unique primary-kind names

Reject multiple distinct primary-kind declarations with the same canonical name across the effective Entity model. Repeated references to one kind are not duplicate declarations; property names and allowed values remain qualified by their bearers and may repeat. Resolve `Module` to its one uniquely named kind. Reject ambiguous names instead of selecting a branch or merging targets. A branch move alone must not invalidate an unchanged unique-name reference. This is a Draft evaluation contract; no parser or project migration has been run.

### General named-relation notation

For a formal Claim or model edge using `Source ((RELATION_TYPE)) Target`, check the matching unescaped delimiters, exact declared Relation Type, endpoint resolution and applicable Entity Definition constraints. Keep the statement distinct from a canonical governing node selector. Unknown type names and unmatched delimiters fail admission rather than becoming new types. A named opposite view uses its defined derived inverse name; the selected short reverse spellings retain their separately governed meanings. No separately authored inverse fact is introduced. Existing short-operator, reference, escape and identity checks remain applicable. CA-A-1240 records the syntax decision; this Draft does not implement a parser or evaluator.

### Exactly-one containment cases

When the applicable endpoint specification states exactly one immediate Whole, reject a contained part instance with no permitted Whole or with more than one. Accept Package/Project Implementation as the parentless root Package and a nested Package under another Package. Reject a Module without exactly one Package when its applicable endpoint specification requires it. Do not infer the number of Modules per Package from the one-parent rule. These are evaluation cases for Draft methodology, not runtime tests.
