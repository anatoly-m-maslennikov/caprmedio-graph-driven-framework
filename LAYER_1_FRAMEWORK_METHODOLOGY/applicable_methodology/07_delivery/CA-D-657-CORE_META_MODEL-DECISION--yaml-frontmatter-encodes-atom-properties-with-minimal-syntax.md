---
atom_id: CA-D-657
ref_id: CA-D-657
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/File
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Actor
tier: 3
status: active
version: 11
updated_at: 2026-11-09 00:57:07 +0400
carrier_destination:
  file:
    name: CA-D-657-CORE_META_MODEL-DECISION--yaml-frontmatter-encodes-atom-properties-with-minimal-syntax.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-657-CORE_META_MODEL-DECISION--yaml-frontmatter-encodes-atom-properties-with-minimal-syntax.md
  source_atom_id: CA-D-657
  source_atom_revision: 11
  source_sha256: 746de474726709cda7f50313e8ee7a7cb137256ead37ec351db6a99865f357ca
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

YAML Frontmatter encodes Atom Properties with minimal syntax

## Claim

### Prose Claim


YAML frontmatter of Markdown Atom carriers.


Preserve the declared Header tree. Encode every name key and named value as lowercase words joined by single underscores; existing underscores and word separators become single underscores. Examples: `Work Report` becomes `work_report`, `Active` becomes `active`, and `IS_WORK_REPORT_FOR` becomes `is_work_report_for`.

Apply name encoding within typed references without changing their syntax or opaque ID tokens. Resolve encoded names against the declared names in the same typed context. Distinct declared names that collapse to the same sibling key or named-value token are invalid; report the collision instead of merging them.

IDs, opaque references, timestamps, numbers, booleans and free text retain their declared data and types. Carrier-owned names and physical locator values retain exact spelling, including Carrier Destination filenames and paths. Quote a string when its YAML spelling would otherwise change its declared type.

Encode each key once and use a YAML sequence for multiple values. Use a nonempty string for each required string; null and collections do not satisfy a scalar requirement. Integers exclude booleans.

Serialize Header keys in the declared Property order, omitting absent optional Properties. Place other admitted Header Properties after the ordered base Properties, with no required order among them. A present Property has a value or, for a group, nonempty children; omit optional empty Properties.

For Markdown Atom carriers:

- Encode Role and Form at their declared Header paths, with name keys such as `role` and `form` and named values such as `plan` and `work_report`. Each value resolves to one declared domain value.
- Encode identity, Ref ID, Version, Status, Updated At, Tier and optional Label at their declared Header paths using the same name rule. Preserve ID and Ref ID values exactly. Apply each Property’s value contract; Summary and Claim remain in Content.
- Encode Topics at its declared Header path with the same recursive name rule. Encode direct Node-instance Relation facts under optional `relations`; each encoded canonical Relation name maps to a nonempty YAML sequence of exact base Atom IDs. A scalar or empty sequence is invalid; omit the group when it has no children. Do not author inverse facts separately.
- Do not encode an Atom Author. Event authorship is governed by the Event Record model.
- Derive Target Scope Unit from the active Subject using the applicable model authority. During carrier migration, `current_scope_unit` and `claim_target_scope_unit`, if present, are legacy compatibility data; they do not establish Atom Properties or override the resolved Scope. Their retention, removal and consistency validation require the selected migration's explicit disposition. Do not infer a target from the carrier directory or use either field as an unverified fallback.
- Place an ordinary RMED Claim in `## Claim` as a container with no direct value. It has one or both `### Formal Claim` and `### Prose Claim` children with unique names. Each child has zero or one direct Markdown value; a Formal Claim value contains a CFEL-labelled code fence. Headings inside a Prose Claim value are not Properties unless an applicable Declaration admits them.

Legacy `content_role`, `type`, `subjects.governs` and `subjects.depends_on` remain readable during migration. Conflicting old and new names for the same Property are invalid in any carrier; equal pairs are readable during transition and do not create duplicate logical values. Compatibility does not make the old names canonical in the migrated model. Existing carriers retain their governed legacy spellings until their mechanical migration is explicitly selected. This policy update does not re-encode those carriers in place.

## Details

The remaining applicable Status, Version, identity, Tier, Label, Summary, conditional-field, Projection, Draft identity and reference constraints remain governed by their own sources. A generated Projection is not an authored source. A new field requires its own applicable authority. Summary and Claim remain body Properties, not frontmatter copies.

### Conditional fields and expansion

- A Plan Header AI Agent Confidence Threshold has zero or one integer values. Encode an explicit value at its declared Header path as an integer; an unselected override remains omitted, and self-sufficiency does **not** copy an inherited value. A Plan Header has no Implementation Retry Limit Property; the retry limit is governed by the Workflow.
- `priority` follows the applicable Concern Priority authority for Concern Atoms **only**. Additional Plan, Operations, proof, **or** other Role-specific fields require an applicable Property Declaration and Delivery encoding; their occurrence **in** old Carriers does **not** admit them.
- The generated `projection` block is admitted **only** **in** a projected representation under the projection source-binding encoding, with **only** its defined `source_carrier_path` String. It is **not** an authored source Atom Property.
- A new field **or** nested key requires applicable authority that settles its canonical location, value type, cardinality, admission condition, **and** permitted values **or** reference resolution. unadmitted fields are invalid; an admitted Property with an unsettled encoding is a schema gap, **not** permission **to** guess **or** report full conformance.
- Apply explicitly governed migration exceptions **only** within their declared boundary. legacy presence alone is **not** an exception; retired fields under the canonical Property location rules remain rejected.

### Subjects-only edit-draft exception

The explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It carries the admitted `<canonical-ID>@<proposed-version>-draft` ID marker (preferred) or compatible `<canonical-ID>@draft` marker at its declared Header path, logical Draft Status encoded as `draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry exactly one Atom ID; marker and filename rules remain governed by the Draft ID marker and Draft filename marker rules. Canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
