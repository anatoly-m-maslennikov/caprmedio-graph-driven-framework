---
subjects:
  governs: Entity/Carrier/File.YAML Frontmatter
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Author
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Actor
version: 1
updated_at: 2026-10-30 03:11:57 +0400
relations: {}
atom_id: CA-D-657@1
content_role: Delivery
type: Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
## Summary

YAML Frontmatter encodes Atom Properties with minimal syntax

## Claim scope

YAML Frontmatter of Markdown Atom Carriers.

## Claim

The YAML Frontmatter of a Markdown Atom Carrier **must** use the least syntax **and** nesting that preserves **all** of the following:

- unambiguous deterministic parsing;
- validation;
- extensibility; **and**
- human readability.

## Details

### Common field encoding

Use the following field encodings for the applicable Atom Properties. Presence follows the applicable Property authority, **not** observed filename tokens. A String is a nonempty YAML string; an Integer excludes Booleans. a null value does **not** satisfy a required Property.

| Property | Top-level field | Encoding **and** applicable presence |
|---|---|---|
| Atom Identity | `atom_id` | String under the Atom ID Carrier definition; exactly one for every Current, Draft, **or** Archived Atom; Draft marker forms follow the Draft ID marker definition; carry Version separately |
| Content Role | `content_role` | **=1** String selecting its canonical Content Role; resolve the admitted domain from applicable authority |
| Type | `type` | **=1** String selecting the Atom's admitted Type under its applicable Type authority; a present field **must not** be null, empty, **or** a collection; filename Type tokens are **not** a second value |
| Local Scope Unit | `current_scope_unit` | **=1** String naming the registered Local Scope Unit that owns an ordinary Atom. For Type Project Goal only, carry its Operator Actor owner through the existing Author fallback under the resolved Target Scope Unit and Project Goal owner encoding; do not register that Actor as a Scope Unit or infer the value from filename |
| Target Scope Unit | `claim_target_scope_unit` | use the resolved Target Scope Unit and Project Goal owner encoding |
| Numeric Tier | `tier` | exactly one integer for every Current Atom under the base Atom Property cardinalities; ordinary Scope Unit-owned Atoms use **>=0** under the Project and non-Project Tier rules, and a verified Project Goal carries exactly `-1` under the Project Goal Tier rule |
| Tier Label | `tier_label` | **0..1** nonempty String for an explicitly carried `Atom.Tier.Label`; retain the integer `tier` field. Use the governed numeric-to-label mapping; omit the Label when not supplied, including for Tiers 5 and higher. This is distinct from the Atom's `label` property. |
| Version **and** Updated At | `version`, `updated_at` | use the Version and Updated At encoding |
| Author | `author` | use the Author encoding |
| Status | `status` | use the Status encoding |
| Label | `label` | **<=1** nonempty String for an explicit Label value; when absent, the effective Label is derived from the Atom Type name under the effective Label rule, without requiring a stored copy of that fallback |
| Summary | no frontmatter copy | exactly one body Property under the Markdown body section rules; its effective value is the nonempty Summary content |
| Claim | no frontmatter copy | exactly one direct prose body Claim for RMED under the Markdown body section rules; R may add one nested Formal claim under the Claim definition |
| Subjects | `subjects` | use the Subjects encoding; **only** the governed Subject keys **and** their admitted encodings |
| authored Atom Relations | `relations` | use the Atom Relations encoding; omission **or** an empty mapping represents no authored Relations; **every** present Relation Kind carries its nonempty target collection |

- `current_scope_unit` **must not** be null, a list, a joined set of names, **or** replaced by an `operators` field. It names the owning Local Scope Unit, except that Type Project Goal carries its Operator Actor owner under the resolved Target Scope Unit and Project Goal owner encoding. This exception does not apply to ordinary Goals. Never infer the value from its filename.
- The Atom ID and Version identify a Current or Archived Atom version under the Atom ID Carrier definition; do **not** duplicate them **in** an `identifier` field. Current, Draft, **and** Archived Atoms carry exactly one Atom ID; a Draft may remain incomplete in other required Properties until promotion. Draft marker forms follow the Draft ID marker definition.
- Every Current Atom satisfies the required and optional base Property cardinalities in the base Atom Property cardinalities. A Draft may be incomplete, but retains its mandatory Atom ID and reports missing required Properties; it must satisfy the full Current contract before promotion.
- Summary **and** Claim use their body sections under the Markdown body section rules, **not** `summary` **or** `claim` frontmatter copies. Other body Properties use their own registered section authority.

### Conditional fields and expansion

- A Plan's explicit `assignee` uses **<=1** String identifying an admitted Actor under the Plan Assignee encoding. `autonomous_confidence_threshold` **and** `implementation_retry_limit` use their integer encodings under the Plan confidence override and retry limit encodings. inherited values remain omitted unless explicitly selected; self-sufficiency does **not** copy them.
- `priority` follows the applicable Concern Priority authority for Concern Atoms **only**. additional Plan, Operations, proof, **or** other Type-specific fields require their applicable Delivery declarations; their occurrence **in** old Carriers does **not** admit them.
- The generated `projection` block is admitted **only** **in** a projected representation under the projection source-binding encoding, with **only** its defined `source_carrier_path` String. It is **not** an authored source Atom Property.
- A new field **or** nested key requires applicable authority that settles its canonical location, value type, cardinality, admission condition, **and** permitted values **or** reference resolution. unadmitted fields are invalid; an admitted Property with an unsettled encoding is a schema gap, **not** permission **to** guess **or** report full conformance.
- Apply explicitly governed migration exceptions **only** within their declared boundary. legacy presence alone is **not** an exception; retired fields under the canonical Property location rules remain rejected.

### Subjects-only edit-draft exception

The explicit source-pinned Subjects-only edit draft is a derived proposed next Revision of an existing Atom, not a new Atom Draft or another canonical original. It may carry `atom_id: <canonical-ID>@<proposed-version>-draft` (preferred) or the compatible `atom_id: <canonical-ID>@draft`, `status: Draft`, and a matching Draft-marker filename in the owning role's `draft/` folder while the exact canonical source remains untouched. The reviewed packet retains the canonical target/source pin and exact draft path/digest for that specific proposed edit. Approval restores the canonical ID and original Status, independently validates normalized Subjects-only materialization, and uses the existing exact predecessor archive plus N+1/actual-time update. Staging and publication require no retained Draft-history entry, `revision_lineage`, unique Draft head, origin chain or consuming successor. New-Atom Drafts and ordinary lifecycle Drafts carry exactly one Atom ID; marker and filename rules remain governed by the Draft ID marker and Draft filename marker rules. Canonical ID grammar and the normal source, schema, identity/collision, permission and exact actual-history safeguards are unchanged.
