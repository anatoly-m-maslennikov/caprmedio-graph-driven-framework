---
atom_id: CA-M-125
ref_id: CA-M-125
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Topics
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Term//Term
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//evaluation_for
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Entity/Property
tier: 3
status: Active
version: 47
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-M-125-CORE_META_MODEL-IMPLEMENTATION_METHOD--assign-subjects-from-the-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Assign Subjects from the Claim

## Claim

### Prose Claim


Subject assignment for an Atom from its Claim **and** complete Markdown Main Content.


**to** assign an Atom's Subjects, the Author **must** perform **all** of:

1. read the entire Markdown Main Content, including Summary, Scope, Claim, Details, other registered sections, nested headings, tables, examples, **and** reference labels. build an inventory of canonical Subject Target mentions with exact locations **and** full resolved paths. treat an Atom citation label rendered under `CA-M-444-CORE_META_MODEL-IMPLEMENTATION_METHOD--atom-claims-expose-their-meaning-conditions-and-consequences-clearly` as the referenced Atom's complete filename **without** its `.md` extension **or** directory path. under `CA-R-1280-CORE_META_MODEL-RULE--reference-every-prerequisite-subject-through-depends-on`, the label is readable reference evidence, **not** a Subject Target mention **or** Subject target, including **when** it occurs **in** the same sentence as Subject Target language; inventory a Subject Target **only** **when** surrounding prose independently uses it.

   recognize an evidenced reusable Term through its authoritative Method Atom of Type Term Definition, including the lexical Term `Term` at `Term//Term`. `Evaluation` remains a Term **when** used inside an Evaluation Atom. use structural definitions, such as `CA-R-1318-CORE_META_MODEL-DEFINITION--define-term` for the Term kind and `CA-R-2514-CORE_META_MODEL-DEFINITION--define-evaluation-content-role` for the Evaluation Content Role, together with the usage context to resolve the referenced Entity target; those structural definitions do **not** replace the lexical meaning owner. self-reference alone does **not** remove a mentioned Subject Target from the inventory **or** establish a new Subject Target; a Term's spelling alone does **not** establish its Subject target. a source-admitted instance name after `//`, a selector literal, **or** syntax is **not** automatically a reusable Term. retain unresolved meaning as an explicit gap rather than treating it as ordinary wording.
2. select the **`=1`** canonical Subject Target that the Claim governs **and** reference its narrowest exact Subject Path directly through GOVERNS.

   - for a Claim about entry **or** exit criteria of a Property, apply this same narrowest-target rule rather than substituting its wider bearer.
   - **when** the Atom has Content Role Evaluation **and** its Claim defines a conformance check, select the canonical target whose conformance is checked; do **not** select a generic Evaluation label **or** the execution of the check merely from its Content Role. bind the checked authority separately with `evaluation_for` under `CA-R-1018-CORE_META_MODEL--register-evaluation-targets`.
3. connect **every** other Subject Target **in** the mention inventory through DEPENDS_ON using its narrowest exact full Subject Path. include mentions outside Claim; do **not** repeat GOVERNS **or** add unmentioned Subject Targets. unresolved mentions block completion rather than disappearing from the inventory.
4. for a definition Claim, use its defined Term **in** the Subject Path that identifies the target being defined, under `CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term`. resolve evidenced reusable lexical components through their Method Term Definitions, while resolving a name after `//` through its instance-naming and source authority rather than automatically requiring a Term Definition; the path identifies the target **and** the GOVERNS link is the Subject Relation. the path does **not** define its component Terms.
5. split the Atom **before** assignment **when** the Claim governs **`>1`** canonical Subject Targets.
6. verify that the distinct GOVERNS **and** DEPENDS_ON targets equal the mention inventory. record **every** reference once **without** creating an intermediate Subject object, repeating definitions, **or** treating path components **and** implicit bearer prefixes as separate Subject Target mentions.
7. serialize the direct references under `CA-D-269-CORE_META_MODEL-DELIVERY--serialize-atom-subjects-in-frontmatter`. its migration-limited legacy compatibility preserves existing temporal carrier evidence; it does **not** add temporal nesting **to** a migrated flat Carrier.
